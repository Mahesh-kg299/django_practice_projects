from rest_framework import serializers
from .models import Video, VTubeUser, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['cmt_text', 'cmt_vid_id', 'cmt_usr_id']
        extra_kwargs = {'cmt_vid_id': {"write_only": True}, 'cmt_usr_id': {"write_only": True}}

class VideoSerializer(serializers.ModelSerializer):
    # comment = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    comment = serializers.SlugRelatedField(read_only=True, many=True, slug_field='cmt_text')
    # comment = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Video
        fields = ['vid_title', 'vid_publish_date', 'vid_views', 'comment']

class VTubeUserSerializer(serializers.ModelSerializer):
    # comment = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    comment = serializers.SlugRelatedField(read_only=True, many=True, slug_field='cmt_text')
    # comment = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = VTubeUser
        fields = ['usr_username', 'usr_password', 'usr_email', 'comment']
        extra_kwargs = {'usr_password':{'write_only': True}}