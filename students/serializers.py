from rest_framework import serializers
from .models import Student
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'password', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', 'groups', 'user_permissions']

class StudentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
        depth = 1

class StudentRetUpdDelSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        depth = 1

class StudentRetUpdDelUserSerializers(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Student
        fields = '__all__'
        depth = 1

    # def update(self, instance, validated_data):
        # user_data = validated_data.pop('user', {})
        # create_batch_data = validated_data.pop('create_batch', [])

        # user_instance = instance.user
        # for key, value in user_data.items():
        #     setattr(user_instance, key, value)
        # user_instance.save()
        # for key, value in validated_data.items():
        #     setattr(instance, key, value)
        # instance.save()
        # instance.create_batch.set(create_batch_data)

        # return instance

class PackageIdwiseStudentGetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"