import json

from django.contrib.auth.models import User
from django.db.models import Sum
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
            # instance.Practise_Exam.objects.
            Studentanswer.objects.filter(user=instance.user, exam=instance.exam)
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
                
@receiver(post_save, sender=Studentanswer)
def check_practice_test_completion(sender, instance, created, **kwargs):
    """
    The function `check_practice_test_completion` is triggered after a `Studentanswer` instance is saved, and it
    checks if the instance is created for a practice test and updates points for a student in a gamification
    system.
    """
    if created and instance.Practise_Exam and instance.exam and not instance.Full_Length_Exam:
        if instance.Practise_Exam.g.exists():
            if instance.Practise_Exam.practice_test_type:
                sets = getattr(instance.Practise_Exam,instance.Practise_Exam.practice_test_type).all()#objects.filter(user=instance.user, exam=instance.exam)
                for exam_block in sets:
                    if not Studentanswer.objects.filter(user=instance.user,exam=exam_block,Practise_Exam=instance.Practise_Exam).exists():
                        return None

                try:
                    getattr(instance.user,'student')
                except AttributeError:
                    return
                        
                pointhistory_object = PointHistory.objects.create(student=instance.user.student,
                                            gamification=instance.Practise_Exam.g.first(),
                                            )
            points = pointhistory_object.gamification.points
            total_points = PointHistory.objects.filter(student=instance.user.student).aggregate(total_points = Sum('gamification__points'))['total_points']
            event = {
                    "type": "points",
                    "points": points,
                    "user_id": instance.user.id,
                    "total_points":total_points,
            }
            connection = get_redis_connection("default")
            payload = json.dumps(event)
            connection.publish("events", payload)