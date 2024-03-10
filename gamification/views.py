from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import FlashCard
from .serializers import FlashCardSerializer


class FlashCardView(ListCreateAPIView):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer 
    
class BadgeViewSet(ModelViewSet):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer
    