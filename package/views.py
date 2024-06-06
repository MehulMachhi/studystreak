from django.shortcuts import render
from .models import Package, UserProfile
from .serializers import (PackageListSerializers, PackageRetUpdDelSerializers, CoursePackageSerializer,EnrollmentSerializer, StudentListSerializers,
EnrollmentPackageSerializer)
from rest_framework import generics
from Courses.models import Course
from students.models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from master.models import batch, CourseMaterial, AdditionalResource,LessonAttachment, LessonAssignment 
from Courses.models import Course 
from package.serializers import PackageListSerializers, PackageListForStudentSerializers, PackageCreateSerializers
from Courses.serializers import CourseListSerializers
from master.serializers import (AdditionalResourceListSerializers, CourseMaterialListSerializers,
LessonAttachmentSerializer,LessonAssignmentSerializer,)
from LiveClass.models import Live_Class
from LiveClass.serializers import LiveClassListSerializer
# from coursedetail.models import Quiz_Question, QuizOption
# from coursedetail.serializers import QuizOptionListSerializers, Quiz_QuestionListSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
from LiveClass.serializers import LiveClassListSerializer

class PackageListView(generics.ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageListSerializers

    # def get_queryset(self):
    #     user = self.request.user
    #     return Package.objects.filter(user_package=user)
    


    # def get(self, request, *args, **kwargs):
    #         queryset = self.get_queryset()
    #         package_count = queryset.count()  
    #         serializer = self.serializer_class(queryset, many=True)
    #         data = {
    #             'packages': serializer.data,
                    # 'package_count': package_count.data
    #         }
    #         return Response(data)

class CoursePackageView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursePackageSerializer
   
################### code work ########################

# class UserWisePackageWithCourseID(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = StudentListSerializers 

#     def get_queryset(self):
#         user = self.request.user
#         return Student.objects.filter(user=user)

#     def get(self, request):
#         queryset = self.get_queryset()
#         package_count = queryset.count()
        
#         package_list = []
       
#         for student in queryset:
#             create_batch = student.create_batch.all() if student.create_batch else None

#             if create_batch:
#                 for batch in create_batch:
                  
#                     if batch.add_package:
                       
#                         package = batch.add_package

                      
#                         serialized_package = PackageListForStudentSerializers(package).data

                       
#                         package_list.append({
#                             'student_id': student.id,
#                             'student_name': student.user.username,
#                             'selected_batch': batch.batch_name,
#                             'package': serialized_package,
#                         })
#                     else:
                       
#                         package_list.append({
#                             'student_id': student.id,
#                             'student_name': student.user.username,
#                             'selected_batch': batch.batch_name,
#                             'package': None,
#                         })
#             else:
               
#                 package_list.append({
#                     'student_id': student.id,
#                     'student_name': student.user.username,
#                     'selected_batch': None,
#                     'package': None,
#                 })

#         data = {
#             'package_count': package_count,
#             'student_packages': package_list,
#         }

#         return Response(data)
    
#################### code work ########################

# lession_question_count = Quiz_Question.objects.filter(lession__in = course.lessons.all()).count()
# lession_option_count = QuizOption.objects.filter(lession__in = course.lessions.all()).count()



#######################################################
#################### code work ########################
#######################################################


class UserWisePackageWithCourseID(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StudentListSerializers

    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(user=user)

    def get(self, request):
        queryset = self.get_queryset()
        package_count = queryset.count()
        package_list = []
        for student in queryset:
            select_batch = student.select_batch.all() if student.select_batch else None
            if select_batch:
                for batch in select_batch:
                    if batch.add_package:
                        package = batch.add_package
                        course = package.select_course 

                        serialized_course = CourseListSerializers(course).data
                        serialized_package = PackageListForStudentSerializers(package).data

                        student_pt_length = len(student.student_pt.all())
                        student_flt_length = len(student.student_flt.all())
                        student_mock_length = len(student.student_mock.all())
                        student_enroll_live_class = student.Live_class_enroll.all()


                        live_class_serializer = LiveClassListSerializer(student_enroll_live_class, many=True)
                        serialized_live_class = live_class_serializer.data

                        package_list.append({
                            'student_id': student.id,
                            'student_name': student.user.username,
                            'student_pt': student_pt_length,
                            'student_flt': student_flt_length,
                            'student_mock': student_mock_length,
                            'selected_batch': batch.batch_name,
                            'batch_id': batch.id,
                            'course': serialized_course,
                            'package': serialized_package,
                            'Live_class_enroll':serialized_live_class
                        })
                    else:
                        package_list.append({
                            'student_id': student.id,
                            'student_name': student.user.username,
                            'student_pt': len(student.student_pt.all()),
                            'student_flt': len(student.student_flt.all()),
                            'student_mock': len(student.student_mock.all()),
                            'selected_batch': batch.batch_name,
                            'batch_id': batch.id,
                            'course': None,
                            'package': None,
                        })
            else:
                package_list.append({
                    'student_id': student.id,
                    'student_name': student.user.username,
                    'student_pt': len(student.student_pt.all()),
                    'student_flt': len(student.student_flt.all()),
                    'student_mock': len(student.student_mock.all()),
                    'selected_batch': None,
                    'batch_id': None,
                    'course': None,
                    'package': None,
                })
        data = {
            'package_count': package_count,
            'student_packages': package_list,
        }
        return Response(data)

################# new code ############

# class UserWisePackageWithCourseID(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = StudentListSerializers 

#     def get_queryset(self):
#         user = self.request.user
#         return Student.objects.filter(user=user)

#     def get(self, request):
#         queryset = self.get_queryset()
#         package_count = queryset.count()
        
#         package_list = []
       
#         for student in queryset:
#             create_batch = student.create_batch.all() if student.create_batch else None

#             if create_batch:
#                 for batch in create_batch:
#                     if batch.add_package:
#                         package = batch.add_package
#                         course = package.select_course  # Get the selected course

#                         # Serialize course information
#                         serialized_course = CourseListSerializers(course).data

#                         # Get and serialize CourseMaterial and AdditionalResource data
#                         course_material_data = CourseMaterial.objects.filter(course=course)
#                         additional_resource_data = AdditionalResource.objects.filter(course=course)

#                         serialized_course_material = CourseMaterialListSerializers(course_material_data, many=True).data
#                         serialized_additional_resource = AdditionalResourceListSerializers(additional_resource_data, many=True).data
#                         serialized_package = PackageListForStudentSerializers(package).data

#                         package_list.append({
#                             'student_id': student.id,
#                             'student_name': student.user.username,
#                             'selected_batch': batch.batch_name,
#                             'course': serialized_course,
#                             'course_material': serialized_course_material,
#                             'additional_resources': serialized_additional_resource,
#                             'package': serialized_package,
#                         })
#                     else:
#                         package_list.append({
#                             'student_id': student.id,
#                             'student_name': student.user.username,
#                             'selected_batch': batch.batch_name,
#                             'course': None,
#                             'course_material': None,
#                             'additional_resources': None,
#                             'package': None,
#                         })
#             else:
#                 package_list.append({
#                     'student_id': student.id,
#                     'student_name': student.user.username,
#                     'selected_batch': None,
#                     'course': None,
#                     'course_material': None,
#                     'additional_resources': None,
#                     'package': None,
#                 })

#         data = {
#             'package_count': package_count,
#             'student_packages': package_list,
#         }

#         return Response(data)



######################### code working | ###############################

# class EnrollPackageView(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self, request, *args, **kwargs):
#         serializer = EnrollmentSerializer(data=request.data)
#         if serializer.is_valid():
#             user = self.request.user

#             try:
#                 student = Student.objects.get(user=user)
#             except Student.DoesNotExist:
#                 return Response({"detail": "Student not found for the authenticated user."}, status=status.HTTP_404_NOT_FOUND)

#             batch_ids = serializer.validated_data.get('batch_ids', [])
#             batches = batch.objects.filter(pk__in=batch_ids)
#             print(f"User: {user}, Student: {student}, Batch IDs: {batch_ids}")

#             already_enrolled_batches = student.select_batch.filter(pk__in=batch_ids)
#             if already_enrolled_batches.exists():
#                 return Response({"detail": f"We are sorry, but you are already enrolled in a batch"},
#                                 status=status.HTTP_400_BAD_REQUEST)

#             new_batches = batches.exclude(pk__in=already_enrolled_batches)
#             student.select_batch.add(*new_batches)

#             print(f"Batches added to select_batch: {new_batches}")

#             return Response({"detail": f"Successfully enrolled  in batches."}, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EnrollPackageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            user = self.request.user

            try:
                student = Student.objects.get(user=user)
            except Student.DoesNotExist:
                return Response({"detail": "Student not found for the authenticated user."}, status=status.HTTP_404_NOT_FOUND)

            batch_ids = serializer.validated_data.get('batch_ids', [])
            batches = batch.objects.filter(pk__in=batch_ids)

            already_enrolled_batches = student.select_batch.filter(pk__in=batch_ids)
            if already_enrolled_batches.exists():
                return Response({"detail": f"We are sorry, but you are already enrolled in a batch"},
                                status=status.HTTP_400_BAD_REQUEST)

            new_batches = batches.exclude(pk__in=already_enrolled_batches)
            student.select_batch.add(*new_batches)

            
            new_batch_count = new_batches.count()

            return Response({"detail": f"Successfully enrolled in {new_batch_count} batches."}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##########################################################
################### packagewiesewnroll ###################
##########################################################

########### code working without self-study logic

# class EnrollPackageStudentView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request, *args, **kwargs):
#         serializer = EnrollmentPackageSerializer(data=request.data)
#         if serializer.is_valid():
#             user = self.request.user

#             try:
#                 student = Student.objects.get(user=user)
#             except Student.DoesNotExist:
#                 return Response(
#                     {"detail": "Student not found for the authenticated user."},
#                     status=status.HTTP_404_NOT_FOUND,
#                 )

#             package_ids = serializer.validated_data.get("package_ids", [])
#             packages = Package.objects.filter(pk__in=package_ids)

#             already_enrolled_packages = student.select_package.filter(
#                 pk__in=package_ids
#             )
#             if already_enrolled_packages.exists():
#                 return Response(
#                     {
#                         "detail": f"We are sorry, but you are already enrolled in a package"
#                     },
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )

#             new_packages = packages.exclude(pk__in=already_enrolled_packages)
#             student.select_package.add(*new_packages)

#             return Response(
#                 {"detail": f"Successfully enrolled in packages."},
#                 status=status.HTTP_201_CREATED,
#             )

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#################################################################
class PackageCreateView(generics.CreateAPIView):

    queryset = Package.objects.all()
    serializer_class = PackageCreateSerializers

class EnrollPackageStudentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = EnrollmentPackageSerializer(data=request.data)
        if serializer.is_valid():
            user = self.request.user

            try:
                student = Student.objects.get(user=user)
            except Student.DoesNotExist:
                return Response(
                    {"detail": "Student not found for the authenticated user."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            
            course_delivery = self.request.data.get("course_delivery")
            if course_delivery == "SELF-STUDY":
                return Response(
                    {"detail": "Self-study courses can be enrolled through this API."},
                    status=status.HTTP_200_OK,
                )

            package_ids = serializer.validated_data.get("package_ids", [])
            course_ids = serializer.validated_data.get("course_ids", [])
            if not package_ids or not course_ids:
                return Response(
                    {"detail": "No package ids and course ids"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            packages = Package.objects.filter(pk__in=package_ids)

            already_enrolled_packages = student.select_package.filter(
                pk__in=package_ids
            )
            if already_enrolled_packages.exists():
                return Response(
                    {
                        "detail": f"We are sorry, but you are already enrolled in a package"
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            new_packages = packages.exclude(pk__in=already_enrolled_packages)
            if not new_packages.exists():
                return Response(
                    {"detail": "No packages found with id"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            student.select_package.add(*new_packages)
            return Response(
                {"detail": f"Successfully enrolled in packages."},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


     
