from rest_framework.serializers import ModelSerializer
from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'dob']

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['media', 'likes_count']
        
class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ['post', 'user']