from django.urls import path
from .views import SaveToken, GoogleVerificationView, state_token
urlpatterns = [
    path('csrf-token',SaveToken.as_view()),
    path('google/',GoogleVerificationView.as_view()),
    path('token/',state_token),
]
