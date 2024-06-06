from django.contrib.auth.models import AnonymousUser, User
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from Courses.models import Course

from .models import Student
from .serializers import (StudentRetUpdDelSerializers,
                          StudentRetUpdDelUserSerializers, StudentSerializers)

# Create your views here.

class StudentView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get_queryset(self):
        user = self.request.user
        # user = request.user
        if isinstance(user, AnonymousUser):
            return Student.objects.none() 

        return Student.objects.filter(user=user)
class StudentRetUpdDelView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentRetUpdDelSerializers



class Student_List_View_Dashboard(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


from django.http import JsonResponse

from master.models import batch
from package.models import Package


# def PackageIdwiseStudentGetView(request, package_id):
#     try:
#         package = Package.objects.get(pk=package_id)
#         students = package.student_set.all() 
#         serialized_students = []  
#         if students.exists():
#             for student in students:
#                 serialized_student = {
#                     'id': student.id,
#                     'user_name': student.user.username,  
#                     'user_first_name': student.user.first_name
#                 }
#                 serialized_students.append(serialized_student)
#             return JsonResponse({'students': serialized_students}, status=200)
#         else:
#             return JsonResponse({'message': 'No students available in package'}, status=200)
#     except Package.DoesNotExist:
#         return JsonResponse({'error': 'Package not found'}, status=404)
    

# def BatchIdwiseStudentGetView(request, batch_id):
#     try:
#         Batch = batch.objects.get(pk=batch_id)
#         students = Batch.student_set.all() 
#         serialized_students = []  
#         if students.exists():
#             for student in students:
#                 serialized_student = {
#                     'id': student.id,
#                     'user_name': student.user.username,  
#                     'user_first_name': student.user.first_name
#                 }
#                 serialized_students.append(serialized_student)
#             return JsonResponse({'students': serialized_students}, status=200)
#         else:
#             return JsonResponse({'message': 'No students available in batch'}, status=200)
#     except batch.DoesNotExist:
#         return JsonResponse({'error': 'Batch not found'}, status=404)
    
def BatchIdwiseStudentGetView(request, batch_id):
    try:
        batch_obj = batch.objects.get(id=batch_id)
        students = batch_obj.student_set.all()
        students_list = []
        if students.exists():
            for student in students:
                serialized_student =  {
                    'id': student.id,
                    'first_name': student.user.first_name,
                    'last_name': student.user.last_name,
                    'gender': student.gender,
                    'country': student.country.name if student.country else None,
                    'state': student.state.name if student.state else None,
                    'city': student.city.name if student.city else None,
                    'phone_no': student.phone_no,
                    'whatsapp_no': student.whatsapp_no,
                    'reference_by': student.reference_by,
                    'country_interested_in': student.country_interested_in.name if student.country_interested_in else None,
                    'last_education': student.last_education,
                    'ielts_taken_before': student.ielts_taken_before,
                    'duolingo_taken_before': student.duolingo_taken_before,
                    'pte_taken_before': student.pte_taken_before,
                    'toefl_taken_before': student.toefl_taken_before,
                    'gre_taken_before': student.gre_taken_before,
                    'gmat_taken_before': student.gmat_taken_before,
                    'remark': student.remark,
                    'biography': student.biography,
                    'user_image': student.user_image.url if student.user_image else None,
                    'interested_in_visa_counselling': student.interested_in_visa_counselling,
                    'select_batch': [batch.batch_name for batch in student.select_batch.all()],
                    'select_package': [package.package_name for package in student.select_package.all()],
                    # 'Live_class_enroll': [live_class.live_class_name for live_class in student.Live_class_enroll.all()],
                    'referal_code': student.referal_code,
                    'created_at': student.created_at.strftime("%Y-%m-%d %H:%M:%S") if student.created_at else None,
                    'updated_at': student.updated_at.strftime("%Y-%m-%d %H:%M:%S") if student.updated_at else None,
                    # 'student_pt': [module.module_name for module in student.student_pt.all()],
                    # 'student_flt': [module.module_name for module in student.student_flt.all()],
                    # 'student_mock': [exam.exam_name for exam in student.student_mock.all()],
                }
                students_list.append(serialized_student)
            return JsonResponse({'students': students_list}, status=200)
        else:
            return JsonResponse({'message': 'No Students are available'}, status=200)
    except batch.DoesNotExist:
        return JsonResponse({'error': 'Batch not found'}, status=404)



import logging

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

logger = logging.getLogger(__name__)

# def CourseIdwiseStudentGetView(self, course_id):
#     try:
#         course = Course.objects.get(id=course_id)
#         students = Student.objects.filter(select_package__select_course=course)

#         students_list = []
#         for student in students:
#             serialized_student = {
#                 'id': student.id,
#                 'first_name': student.user.first_name,
#                 'last_name': student.user.last_name,
#                 'gender': student.gender,
#                 'country': student.country.name if student.country else None,
#                 'state': student.state.name if student.state else None,
#                 'city': student.city.name if student.city else None,
#                 'phone_no': student.phone_no,
#                 'whatsapp_no': student.whatsapp_no,
#                 'reference_by': student.reference_by,
#                 'country_interested_in': student.country_interested_in.name if student.country_interested_in else None,
#                 'last_education': student.last_education,
#                 'ielts_taken_before': student.ielts_taken_before,
#                 'duolingo_taken_before': student.duolingo_taken_before,
#                 'pte_taken_before': student.pte_taken_before,
#                 'toefl_taken_before': student.toefl_taken_before,
#                 'gre_taken_before': student.gre_taken_before,
#                 'gmat_taken_before': student.gmat_taken_before,
#                 'remark': student.remark,
#                 'biography': student.biography,
#                 'user_image': student.user_image.url if student.user_image else None,
#                 'interested_in_visa_counselling': student.interested_in_visa_counselling,
#                 'select_batch': [batch.batch_name for batch in student.select_batch.all()],
#                 'select_package': [package.package_name for package in student.select_package.all()],
#                 'referal_code': student.referal_code,
#                 'created_at': student.created_at.strftime("%Y-%m-%d %H:%M:%S") if student.created_at else None,
#                 'updated_at': student.updated_at.strftime("%Y-%m-%d %H:%M:%S") if student.updated_at else None,
#                 # 'student_pt': [module.module_name for module in student.student_pt.all()],
#                 # 'student_flt': [module.module_name for module in student.student_flt.all()],
#                 # 'student_mock': [exam.exam_name for exam in student.student_mock.all()],
#             }
#             students_list.append(serialized_student)

#         if students_list:
#             return JsonResponse({'students': students_list}, status=200)
#         else:
#             return JsonResponse({'message': 'No students are available for the course'}, status=200)
#     except ObjectDoesNotExist:
#         return JsonResponse({'error': 'Course not found'}, status=404)
#     except ZeroDivisionError:
#         return JsonResponse({'message':'student '})
#     except Exception as e:
#         logger.error(f"An unexpected error occurred: {str(e)}")
#         return JsonResponse({'error': 'An unexpected error occurred'}, status=500) 
    

