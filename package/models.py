# package/models.py

from django.db import models
from Courses.models import Course
from master.models import PackageType
from django.contrib.auth.models import User

# Section: Package
class Package(models.Model):
    user_package = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    package_name = models.CharField(max_length=255, blank=True)
    package_price = models.CharField(
        max_length=100, null=True, blank=True
    )  # Should this be DecimalField or IntegerField for an actual price?
    PackageType = models.ForeignKey(PackageType, on_delete=models.CASCADE, null=False)
    select_course = models.ForeignKey(Course, on_delete=models.CASCADE)

    # Section: MATERIAL
    soft_copy = models.BooleanField(default=False)
    hard_copy = models.BooleanField(default=False)

    # Section: TESTING
    full_length_test = models.BooleanField(default=False)
    full_length_test_count = models.PositiveIntegerField(default=0)
    practice_test = models.BooleanField(default=False)
    practice_test_count = models.PositiveIntegerField(default=0)
    speaking_test = models.BooleanField(default=False)
    speaking_test_count = models.PositiveIntegerField(default=0)

    writing_evaluation = models.BooleanField(default=False)
    # Section: MEMBERSHIP
    live_classes_membership = models.BooleanField(default=False)
    online_membership = models.BooleanField(default=False)
    offline_membership = models.BooleanField(default=False)

    # Section: DOUBT SOLVING
    group_doubt_solving = models.BooleanField(default=False)
    group_doubt_solving_count = models.PositiveIntegerField(default=0)
    one_to_one_doubt_solving = models.BooleanField(default=False)
    one_to_one_doubt_solving_count = models.PositiveIntegerField(default=0)
    validity = models.DateTimeField(null=True, blank=True)
    duration = models.PositiveIntegerField(help_text="in_months", null=True, blank=True)
    coupon_code = models.ForeignKey(
        "master.Cupon", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.package_name


from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .models import UserProfile

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)