from rest_framework import generics, viewsets, views
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Company, Industry
from .serializers import CompanySerializer, IndustrySerializer, UserSerializer
from django.contrib.auth.models import User
# Create your views here.


# class CompanyList(generics.ListAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer

# class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer


# class IndustryList(generics.ListAPIView):
#     queryset = Industry.objects.all()
#     serializer_class = IndustrySerializer

# class IndustryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Industry.objects.all()
#     serializer_class = IndustrySerializer



class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer