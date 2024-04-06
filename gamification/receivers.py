from django.db.models.signals import post_save
from django.dispatch import receiver

from Create_Test.models import FullLengthTest
from ExamResponse.models import Studentanswer

from .utils import save_points_and_publish_message


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
        and instance.exam.g.exists()
    ):
        save_points_and_publish_message(instance.exam.g.all().first(), instance.user)


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

        try:
            getattr(instance.user, "student")
        except AttributeError:
            return

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

        save_points_and_publish_message(
            instance.Practise_Exam.g.all().first(), instance
        )


@receiver(post_save, sender=Studentanswer, dispatch_uid="00x123")
def check_FLT_submission(sender, instance, created, **kwargs):
    if (
        created
        and instance.Full_Length_Exam
        and not instance.Practise_Exam
        and instance.exam
        and instance.Full_Length_Exam.g.exists()
    ):
        try:
            getattr(instance.user, "student")
        except AttributeError:
            return

        exam_blocks = FullLengthTest.objects.filter(
            id=instance.Full_Length_Exam.id
        ).values_list(
            "reading_set__Reading",
            "speaking_set__Speaking",
            "listening_set__Listening",
            "writing_set__Writing",
        )

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

        gamification_object = instance.Full_Length_Exam.g.first()

        save_points_and_publish_message(gamification_object, instance.user)
