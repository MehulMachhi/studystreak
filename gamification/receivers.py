import json

from django.db.models import Sum
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_redis import get_redis_connection

from Create_Test.models import FullLengthTest
from ExamResponse.models import Studentanswer
from gamification.models import PointHistory


@receiver(post_save, sender=Studentanswer)
def check_exam_completion(sender, instance, created, **kwargs):
    """
    The function `check_exam_completion` is triggered after a `Studentanswer` instance is saved, and it
    checks if the instance is created for an exam and updates points for a student in a gamification
    system.
    """
    if (
        created
        and instance.exam
        and not instance.Practise_Exam
        and not instance.Full_Length_Exam
    ):
        # instance.Practise_Exam.objects.
        Studentanswer.objects.filter(user=instance.user, exam=instance.exam)
        if instance.exam.g.exists():
            PointHistory.objects.create(
                student=instance.user.student,
                gamification=instance.exam.g.first(),
            )
            points = instance.exam.g.first().points
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
    if (
        created
        and instance.Practise_Exam
        and instance.exam
        and not instance.Full_Length_Exam
        and instance.Practise_Exam.g.exists()
        and instance.Practise_Exam.practice_test_type
    ):

        sets = getattr(
            instance.Practise_Exam, instance.Practise_Exam.practice_test_type
        ).all()

        for exam_block in sets:
            if not Studentanswer.objects.filter(
                user=instance.user,
                exam=exam_block,
                Practise_Exam=instance.Practise_Exam,
            ).exists():
                return None

        try:
            getattr(instance.user, "student")
        except AttributeError:
            return

        pointhistory_object = PointHistory.objects.create(
            student=instance.user.student,
            gamification=instance.Practise_Exam.g.first(),
        )
        points = pointhistory_object.gamification.points

        total_points = PointHistory.objects.filter(
            student=instance.user.student
        ).aggregate(total_points=Sum("gamification__points"))["total_points"]
        event = {
            "type": "points",
            "points": points,
            "user_id": instance.user.id,
            "total_points": total_points,
        }
        connection = get_redis_connection("default")
        payload = json.dumps(event)
        connection.publish("events", payload)




@receiver(post_save, sender=Studentanswer,dispatch_uid='00x123')
def check_FLT_submission(sender, instance, created, **kwargs):
    if (
        created
        and instance.Full_Length_Exam
        and not instance.Practise_Exam
        and instance.exam
        and instance.Full_Length_Exam.g.exists()
    ):
        exam_blocks = FullLengthTest.objects.filter(
            id=instance.Full_Length_Exam.id).values_list(
                'reading_set__Reading','speaking_set__Speaking',
                'listening_set__Listening','writing_set__Writing')
        
        # unpack ids 
        unpack_ids = list(map(lambda x: (i for i in x), exam_blocks))
        
        # check if the answer exists for other exam_blocks
        for id in unpack_ids:
            if not Studentanswer.objects.filter(
                exam__id=id,
                Full_Length_Exam=instance.Full_Length_Exam,
                user=instance.user,
            ).exists():
                return
            
            
        # OLD LOGIC 
        
        # flt_instance = instance.Full_Length_Exam
        # for practice_set in flt_instance.reading_set.all():
        #     for exam_block in practice_set:
        #         if not Studentanswer.objects.filter(
        #             exam=exam_block,
        #             Practise_Exam=practice_set,
        #             Full_Length_Exam=flt_instance,
        #             user=instance.user,
        #         ).exists():
        #             return

        # for practice_set in flt_instance.listening_set.all():
        #     for exam_block in practice_set:
        #         if not Studentanswer.objects.filter(
        #             user=instance.user,
        #             exam=exam_block,
        #             Practise_Exam=practice_set,
        #             Full_Length_Exam=flt_instance,
        #         ).exists():
        #             return

        # for practice_set in flt_instance.speaking_set.all():
        #     for exam_block in practice_set:
        #         if not Studentanswer.objects.filter(
        #             user=instance.user,
        #             exam=exam_block,
        #             Practise_Exam=practice_set,
        #             Full_Length_Exam=flt_instance,
        #         ).exists():
        #             return

        # for practice_set in flt_instance.writing_set.all():
        #     for exam_block in practice_set:
        #         if not Studentanswer.objects.filter(
        #             user=instance.user,
        #             exam=exam_block,
        #             Practise_Exam=practice_set,
        #             Full_Length_Exam=flt_instance,
        #         ).exists():
        #             return

        try:
            getattr(instance.user, "student")
        except AttributeError:
            return

        pointhistory_object = PointHistory.objects.create(
            student=instance.user.student,
            gamification=instance.Full_Length_Exam.g.first(),
        )
        points = pointhistory_object.gamification.points

        total_points = instance.user.student.pointhistory.aggregate(total = Sum('gamification__points'))['total']
        event = {
            "type": "points",
            "points": points,
            "user_id": instance.user.id,
            "total_points": total_points,
        }

        connection = get_redis_connection("default")
        payload = json.dumps(event)
        connection.publish("events", payload)
