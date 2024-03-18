from rest_framework import serializers
from .models import Package
from Courses.models import Course
from master.models import Cupon, PackageType
from students.models import Student
from master.models import batch

class StudentListSerializers(serializers.ModelSerializer):
   
    class Meta:
        model = Student
        fields = '__all__'
        depth = 2
        

class PackageListSerializers(serializers.ModelSerializer):
   
    class Meta:
        model = Package
        fields = '__all__'
        depth = 1

################ only create foe Student batch wise package get ###############
class PackageListForStudentSerializers(serializers.ModelSerializer):
   
    class Meta:
        model = Package
        fields = '__all__'
        # depth = 1
        
class PackageRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'
        depth = 1

class CuponCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cupon
        fields = ('cupon_name', 'cupon_code', 'campaign_name', 'discount', 'start_date', 'end_date')

class PackageCourseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageType
        fields = ('name',)

class CourseCoursePackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'Course_Title']

class CoursePackageSerializer(serializers.ModelSerializer):
    packages = serializers.SerializerMethodField()
    
    class Meta:
        model = Course
        fields = ['id', 'Course_Title', 'packages'] 

    def get_packages(self, obj):
        return [
            {'package_id': package.id,'package_name': package.package_name, 'package_price': package.package_price, 'soft_copy': package.soft_copy, 
            'hard_copy': package.hard_copy, 'full_length_test': package.full_length_test, 'full_length_test_count': package.full_length_test_count,
            'practice_test': package.practice_test, 'practice_test_count': package.practice_test_count, 'speaking_test': package.speaking_test,
            'speaking_test_count': package.speaking_test_count, 'writing_evaluation': package.writing_evaluation,
            'live_classes_membership':package.live_classes_membership, 'online_membership': package.online_membership, 'offline_membership':package.offline_membership,
            'group_doubt_solving': package.group_doubt_solving, 'group_doubt_solving_count': package.group_doubt_solving_count, 
            'one_to_one_doubt_solving': package.one_to_one_doubt_solving, 'one_to_one_doubt_solving_count': package.one_to_one_doubt_solving_count, 
            'validity': package.validity, 'duration': package.duration, 'coupon_code': CuponCourseSerializer(package.coupon_code).data,
            'PackageType': PackageCourseTypeSerializer(package.PackageType).data,
            'select_course': CourseCoursePackageSerializer(package.select_course).data} 
            for package in obj.package_set.all()]



class EnrollmentPackageSerializer(serializers.ModelSerializer):
    package_ids = serializers.ListField(child=serializers.CharField(), required=True)
    course_ids = serializers.ListField(child=serializers.IntegerField(), required=True)
    class Meta:
        model = Package
        fields ="__all__"
        depth = 1


class PackageCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = "__all__"

class EnrollmentSerializer(serializers.Serializer):
    batch_ids = serializers.ListField(child=serializers.CharField(), required=True)
   
    class Meta:
        model = batch
        fields = ("id", "batch_name", "batch_startdate", "batch_enddate", "batch_start_timing", "batch_end_timing", "add_package",)
        depth = 1

# from rest_framework import serializers
# from django.contrib.auth.models import User
# from .models import UserProfile

# class UserRegistrationSerializer(serializers.ModelSerializer):
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         user_profile = UserProfile.objects.create(user=user)

#         return user