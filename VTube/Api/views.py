from rest_framework import generics, permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Video, VTubeUser, Comment
from .serializers import VideoSerializer, VTubeUserSerializer, CommentSerializer

# Create your views here.

class VideoListView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VTubeUserListView(generics.ListCreateAPIView):
    queryset = VTubeUser.objects.all()
    serializer_class = VTubeUserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VTubeUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VTubeUser.objects.all()
    serializer_class = VTubeUserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class RegisterUserView(APIView):
    def post(self, request, format = None):
        user = User.objects.create(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        return Response({'status': 'User registered succussfully'})