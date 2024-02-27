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

# Create your views here.


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

from students.models import Student
class UpdateStudentFields(APIView):
    permission_classes = []
    authentication_classes = []

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
            student_pt_data = {'Name': module_instance.Name} 
            student_instance.student_pt.create(**student_pt_data)
        elif typetest == 'Full Length':
            student_flt_data = {'Name': module_instance.Name}  
            student_instance.student_flt.create(**student_flt_data)
        else:
            return Response({"detail": "Invalid Typetest"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"detail": "Student fields updated successfully"}, status=status.HTTP_200_OK)