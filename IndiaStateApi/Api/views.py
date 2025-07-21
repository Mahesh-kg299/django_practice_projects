from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import State, ChfMinister
from .serializers import StateSerializer, ChfMinisterSerializer
# Create your views here.

class StateList(generics.ListCreateAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class StateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class ChfMinisterList(generics.ListCreateAPIView):
    queryset = ChfMinister.objects.all()
    serializer_class = ChfMinisterSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

class ChfMinisterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChfMinister.objects.all()
    serializer_class = ChfMinisterSerializer

