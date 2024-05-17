from django.urls import path
from .views import SaveToken, GoogleVerificationView
urlpatterns = [
    path('csrf-token',SaveToken.as_view()),
    path('google/',GoogleVerificationView.as_view()),
    # path('token/',state_token),
]
