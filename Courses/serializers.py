from rest_framework import serializers

from .models import Course
from master.serializers import AdditionalResourceListSerializers, CourseMaterialListSerializers
from coursedetail.serializers import LessonListSerializers, LessonDetailSerializer
from django.contrib.auth.models import User

class CourseListSerializers(serializers.ModelSerializer):
    lessons = LessonListSerializers(many=True, read_only=True)
    course_materials = CourseMaterialListSerializers(many=True, read_only=True)
    additional_resources = AdditionalResourceListSerializers(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

        depth = 2


class CourseCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseRetUpdDelSerializers(serializers.ModelSerializer):
    lessons = LessonDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
        depth = 4

    # def get_tutor(self, obj):
    #     tutors = obj.tutor.all()
    #     return UserSerializer(tutors, many=True).data if tutors else None
    # class Meta:
    #     model = Course
    #     fields = "__all__"

        
############################# Course List Serializers // for use in package model ########################

class Course_List_Serializers_forpackage(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
        depth=2
       
        
class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'