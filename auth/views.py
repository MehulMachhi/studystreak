
from django.http import HttpResponse
from django.shortcuts import redirect
import requests
from auth.serializers import GoogleVerificationSerializer
from studystreak_api.utils import get_user_role
from studystreak_api.views import LoginView, get_tokens_for_user
from utils.views import PublicAPI
from rest_framework.response import Response
from django.middleware.csrf import get_token
from django.core.cache import cache
import random
from django.conf import settings
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from django.contrib.auth.models import User, Group
class SaveToken(PublicAPI):
    
    def get(self, request, *args, **kwargs):
        rand_id = ''
        for _ in range(10):
            rand_id = rand_id + str((random.randint(1,9)))
            
        state_token = get_token(request)
        cache.set(rand_id,state_token,60 *2)
        return Response(f'{rand_id}-{state_token}',200)

def state_token(request):
    return redirect(
        f"https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id=777985082123-96jf0j19a69tgbm5gcpso61q19rl31d2.apps.googleusercontent.com&scope=email profile&redirect_uri=http://localhost:8000/api/google/&state={'state'}"
    )

class GoogleVerificationView(PublicAPI):
    def get(self, request, *args, **kwargs):
        serializer = GoogleVerificationSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            rcvd_token = serializer.id_token
            id_info = id_token.verify_oauth2_token(rcvd_token, google_requests.Request(), settings.GOOGLE_CLIENT_ID)
            print(id_info)
            user, created = User.objects.get_or_create(
                email= id_info['email'],
                first_name = id_info['given_name'],
                last_name = id_info['family_name'],                
            )
            
            token = get_tokens_for_user(user)
            user_role = get_user_role(user)
            try:
                user_group = (Group.objects.get(user=user.id)).name
            except Exception:
                user_group = "None"
            
            return Response(
                    {
                        "token": token,
                        "msg": "Login Successful",
                        "userid": user.id,
                        "user_status": user_group,
                        "user_role": user_role,
                    },
                    status=200,
                )
                
def callback(request):
    print(request.GET.get('code'))
    return HttpResponse('ddd')