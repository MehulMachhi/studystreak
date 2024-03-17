import json

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_redis import get_redis_connection

from ExamResponse.models import Studentanswer
from gamification.models import Gamification, PointHistory
from students.models import Student


@receiver(post_save, sender=Studentanswer)
def check_exam_completion(sender, instance, created, **kwargs):
    """
    The function `check_exam_completion` is triggered after a `Studentanswer` instance is saved, and it
    checks if the instance is created for an exam and updates points for a student in a gamification
    system.
    """
    
    if created and instance.exam and not instance.Practise_Exam and not instance.Full_Length_Exam:
            student = Student.objects.first()
            if instance.exam.g.exists():
                PointHistory.objects.create(student=instance.user.student,
                                            gamification=instance.exam.g.first(),
                                            )
                points = instance.exam.g.first().points
                print(f"{points} Points added")
                event = {
                     "type": "points",
                     "points": points,
                     "user_id": instance.user.id,
                }
                connection = get_redis_connection("default")
                payload = json.dumps(event)
                connection.publish("events", payload)
                # Now Emit the websocket event to update the points in the frontend