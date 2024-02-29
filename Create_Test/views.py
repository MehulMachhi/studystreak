# Create your views here.
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Responses, createexam, module
from .serializers import (
    ModuleCreateSerializers,
    ModuleListSerializers,
    ResponsesSerializers,
    createexamserializers,
)
from students.models import Student
# Create your views here.
from exam.models import Exam

class createexamview(generics.ListCreateAPIView):
    queryset = createexam.objects.all()
    serializer_class = createexamserializers


class ResponsesView(generics.ListCreateAPIView):
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerializers



class moduleListView(generics.ListCreateAPIView):
    queryset = module.objects.all()
    serializer_class = ModuleListSerializers

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ModuleCreateSerializers
        return super().get_serializer_class()


class UpdateStudentFields(APIView):

    def post(self, request):
        student_id = request.data.get('student_id')
        module_id = request.data.get('module_id')
        typetest = request.data.get('typetest')
        
        try:
            student_instance = Student.objects.get(pk=student_id)
        except Student.DoesNotExist:
            return Response({"detail": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            module_instance = module.objects.get(pk=module_id)
        except module.DoesNotExist:
            return Response({"detail": "Module not found"}, status=status.HTTP_404_NOT_FOUND)
      
        if typetest == 'Practice':
            existing_exams = student_instance.student_pt.filter(Name=module_instance.Name)
        elif typetest == 'Full Length':
            existing_exams = student_instance.student_flt.filter(Name=module_instance.Name)
       
        else:
            return Response({"detail": "Invalid Typetest"}, status=status.HTTP_400_BAD_REQUEST)
        
        if existing_exams.exists():
            return Response({"detail": "The exam already add"}, status=status.HTTP_400_BAD_REQUEST)
            # return Response({"detail": f"The {typetest} exam '{module_instance.Name}' already add"}, status=status.HTTP_400_BAD_REQUEST)
    
        if typetest == 'Practice':
            student_pt_data = {'Name': module_instance.Name} 
            student_instance.student_pt.create(**student_pt_data)
        elif typetest == 'Full Length':
            student_flt_data = {'Name': module_instance.Name}  
            student_instance.student_flt.create(**student_flt_data)
        
        
        return Response({"detail": "Student fields updated successfull"}, status=status.HTTP_200_OK)
    
# class MockTestStudentSubmit(APIView):
    # def post(self, request):
    #     student_id = request.data.get("student_id")
    #     exam_id = request.data.get("exam_id")
    #     typetest = request.data.get("typetest")

    #     try:
    #         student_instance = Student.objects.get(pk=student_id)
    #     except Student.DoesNotExist:
    #         return Response({"detail": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

    #     try:
    #         module_instance = Exam.objects.get(pk=exam_id)
    #     except Exam.DoesNotExist:
    #         return Response({"details": "Exam not found"}, status=status.HTTP_404_NOT_FOUND)

    #     if typetest == "Mock Test":
    #         existing_students = Student.objects.filter(student_mock__exam_name=module_instance.exam_name)
    #         if existing_students.exists():
    #             return Response({"detail": "students are already add"}, status=status.HTTP_400_BAD_REQUEST)

    #         student_mock_data = {"exam_name": module_instance.exam_name}
    #         student_instance.student_mock.create(**student_mock_data)
    #     else:
    #         return Response({"detail": "Invalid TypeTest"}, status=status.HTTP_400_BAD_REQUEST)

    #     return Response({"details": "Student Updated Successfully"}, status=status.HTTP_200_OK)

class MockTestStudentSubmit(APIView):
    def post(self, request):
        student_id = request.data.get("student_id")
        exam_id = request.data.get("exam_id")
        typetest = request.data.get("typetest")

        try:
            student_instance = Student.objects.get(pk=student_id)
        except Student.DoesNotExist:
            return Response({"detail": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            module_instance = Exam.objects.get(pk=exam_id)
        except Exam.DoesNotExist:
            return Response({"details": "Exam not found"}, status=status.HTTP_404_NOT_FOUND)

        if typetest == "Mock Test":
            existing_students = student_instance.student_mock.filter(exam_name=module_instance.exam_name)
            if existing_students.exists():
                return Response({"detail": "This student is already associated with this exam"}, status=status.HTTP_400_BAD_REQUEST)

            student_instance.student_mock.add(module_instance)
        else:
            return Response({"detail": "Invalid TypeTest"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"details": "Student Updated Successfully"}, status=status.HTTP_200_OK)