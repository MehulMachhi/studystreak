from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FlashCard, Gamification
from .serializers import FlashCardSerializer, GamificationSerializer


class FlashCardView(ListCreateAPIView):
    queryset = FlashCard.objects.all()
    serializer_class = FlashCardSerializer
    
class gamificationCreateView(APIView):
    def post(self, request):
        serializer = GamificationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("bad request", status=status.HTTP_201_CREATED)
        