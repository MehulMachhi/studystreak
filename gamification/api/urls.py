from django.urls import path
from .views import BadgeViewSet, FlashCardView, GamificationViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('badges',BadgeViewSet,basename='badge')
router.register('',GamificationViewSet,basename='gamification')

urlpatterns = [
    
    path("flashcard/",FlashCardView.as_view()),
] + router.urls

