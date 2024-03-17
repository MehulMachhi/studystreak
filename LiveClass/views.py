import json

from django.conf import settings
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView
from zoomus import ZoomClient

from master.models import batch
from students.models import Student
from zoomApi.zoomAPI import ZOomClient

from .models import Live_Class
from .serializers import (LiveClassCreateSerializer, LiveClassListSerializer,
                          LiveClassListWithIDSerializer)

base_url = 'https://zoom.us'
token_url = "https://zoom.us/oauth/token"
Account_id = "4h9jZgnETeC1jeCttAqewA"
client_id = "uWxvDYmLRBGf6uW2HUWgA"
client_secret = "B8Xg5H6UJbjppdTptwa2IOjn6mQaFsBs"
client = ZoomClient(client_id, client_secret, Account_id)

class LiveClassUsersView(APIView):
    def get(self, request):
        user_list_response = client.user.list()
        user_list = json.loads(user_list_response.content)
        return JsonResponse( data=user_list, status= 200)
    
class LiveClassListView(APIView):
    def get(self, request):
        list_meeting = client.meeting.list(user_id="jP0UzREKQdaFADMVsxTRlA")
        return JsonResponse(data=list_meeting.json(), status =200)
    
    def post(self, request):
        meeting_list = client.meeting.create(user_id="jP0UzREKQdaFADMVsxTRlA", json={
            'topic': 'My Zoom Meeting 1',
            'type': 2,  # 1 for instant meeting, 2 for scheduled meeting
            'password': 'YourMeetingPassword12345'
        })
        print("meeting_list",meeting_list.json())
        return JsonResponse(data= meeting_list.json(), status=200)
        
        
class liveclass_list_view(generics.ListAPIView):
    # queryset = Live_Class.objects.all().order_by('-id')
    queryset = Live_Class.objects.all().order_by('-start_time')
    serializer_class = LiveClassListSerializer


class Liveclass_Create_View(generics.ListCreateAPIView):
    queryset = Live_Class.objects.all()
    serializer_class = LiveClassCreateSerializer
    zc = ZOomClient(settings.ACCOUNT_ID, settings.CLIENT_ID, settings.CLIENT_SECRET)
    
# {
#     "id": 1,
#     "meeting_title": "IELTS ESSIENTIALS DAY 2",
#     "meeting_description": "SDFDASF",
#     "start_time": "2024-02-18T14:30:00+05:30",
#     "end_time": "2024-02-18T15:30:00+05:30",
#     "zoom_meeting_id": "https://meet.google.com/tpk-bihj-snm",
#     "zoom_meeting_password": "",
#     "select_batch": null,
#     "liveclasstype": null
# }
    def create(self, request, *args, **kwargs):

        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        data = serializer.validated_data
        formatted_string = data['start_time'].strftime("%Y-%m-%dT%H:%M:%S")
        zoom_data = {
            "agenda":data['meeting_description'],
            'topic':data['meeting_title'],
            "start_time": formatted_string,
            "timezone": "Asia/Kolkata",
            "password": data['zoom_meeting_password'],
            "email_notification":True,
            'approval_type':0,
            "close_registration":True
        }
        try:
            zoom_returned_data = self.zc.create_meeting(zoom_data)
            data['zoom_meeting_id'] = zoom_returned_data['join_url']
        except Exception:
            return 
        return super().perform_create(serializer)


from django.shortcuts import get_object_or_404

from students.serializers import StudentSerializers


class liveclass_listwithid_view(generics.ListAPIView):
    serializer_class = LiveClassListWithIDSerializer

    def get_queryset(self):
        batch_id = self.kwargs.get('batch_id')
        batch_instance = get_object_or_404(batch, id=batch_id)
        return Live_Class.objects.filter(select_batch=batch_instance)





################## code work ########################
class StudentLiveClassEnrollmentAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def post(self, request, *args, **kwargs):
        live_class_id = request.data.get('live_class_id')
        student_id = request.data.get('student_id')

        try:
            live_class_instance = Live_Class.objects.get(id=live_class_id)
            student_instance = Student.objects.get(id=student_id)

            #enroll code add
            if live_class_instance in student_instance.Live_class_enroll.all():
                    return Response({"Message": "You are already enrolled "}, status=status.HTTP_400_BAD_REQUEST)

            student_instance.Live_class_enroll.add(live_class_instance)

            serializer = StudentSerializers(student_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Live_Class.DoesNotExist:
            return Response({"error": "Live_Class not found"}, status=status.HTTP_404_NOT_FOUND)

        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        

########################### new code #################################
# class StudentLiveClassEnrollmentAPIView(generics.UpdateAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializers

#     def post(self, request, *args, **kwargs):
#         live_class_id = request.data.get('live_class_id')
#         student_id = request.data.get('student_id')

#         try:
#             live_class_instance = Live_Class.objects.get(id=live_class_id)
#             student_instance = Student.objects.get(id=student_id)

#             # Check if the student is already enrolled in the live class
#             if live_class_instance in student_instance.Live_class_enroll.all():
#                 return Response({"error": "Student is already enrolled in this Live_Class"}, status=status.HTTP_400_BAD_REQUEST)

#             # Add the Live_Class instance to the Live_class_enroll field
#             student_instance.Live_class_enroll.add(live_class_instance)

#             serializer = StudentSerializers(student_instance)
#             return Response(serializer.data, status=status.HTTP_200_OK)

#         except Live_Class.DoesNotExist:
#             return Response({"error": "Live_Class not found"}, status=status.HTTP_404_NOT_FOUND)

#         except Student.DoesNotExist:
#             return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)


###########################################################################


class StudentRemoveLiveClassAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def post(self, request, *args, **kwargs):
        live_class_id = request.data.get('live_class_id')
        student_id = kwargs.get('pk')  

        try:
            live_class_instance = Live_Class.objects.get(id=live_class_id)
            student_instance = Student.objects.get(id=student_id)

          
            if live_class_instance in student_instance.Live_class_enroll.all():
                student_instance.Live_class_enroll.remove(live_class_instance)
                serializer = StudentSerializers(student_instance)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"Message": "Student is not enrolled in this Live_Class"}, status=status.HTTP_400_BAD_REQUEST)

        except Live_Class.DoesNotExist:
            return Response({"error": "Live_Class not found"}, status=status.HTTP_404_NOT_FOUND)

        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)