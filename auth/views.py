from django.http import JsonResponse
from django.shortcuts import redirect
from auth.serializers import GoogleAUthVerifiedData, GoogleVerificationSerializer
from studystreak_api.utils import get_user_role
from studystreak_api.views import get_tokens_for_user
from utils.views import PublicAPI
from rest_framework.response import Response
from django.middleware.csrf import get_token
from django.core.cache import cache
import random
from django.contrib.auth.models import Group


class SaveToken(PublicAPI):
    def get(self, request, *args, **kwargs):
        rand_id = ""
        for _ in range(10):
            rand_id = rand_id + str((random.randint(1, 9)))

        state_token = get_token(request)
        cache.set(rand_id, state_token, 60 * 5)
        return Response(f"{rand_id}-{state_token}", 200)


def state_token(request):
    return redirect(
        f"https://accounts.google.com/o/oauth2/v2/auth?response_type=code&client_id=777985082123-96jf0j19a69tgbm5gcpso61q19rl31d2.apps.googleusercontent.com&scope=email profile&redirect_uri=http://localhost:8000/api/google/&state={'state'}"
    )


class GoogleVerificationView(PublicAPI):
    def get(self, request, *args, **kwargs):
        serializer = GoogleAUthVerifiedData(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
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
    print(code := (request.GET.get("code")))

    s = GoogleVerificationSerializer(data={"code": code})
    if s.is_valid():
        return JsonResponse(s.id_token, safe=False)
