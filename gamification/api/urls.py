from django.urls import path
from .views import BadgeViewSet, GamificationViewSet, FlashCardViewSet, Notification, PointHistoryViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('badges',BadgeViewSet,basename='badge')
router.register('',GamificationViewSet,basename='gamification')
router.register('flashcard',FlashCardViewSet,basename='flashcard')
router.register('points',PointHistoryViewSet,basename='pointhistory')


urlpatterns = [
    path('notification/',Notification),
    
] + router.urls

