from accounts.models import Trainer, Client
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import TrainerSerializer

class TrainerView(generics.ListAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class TrainerDetailView(APIView):
    def get(self, request, pk):
        trainer = Trainer.objects.get(pk=pk)
        serializer = TrainerSerializer(trainer)
        return Response(serializer.data)