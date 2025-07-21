from django.db import models

# Create your models here.
class Video(models.Model):
    vid_id = models.AutoField(primary_key=True)
    vid_title = models.CharField(max_length=50)
    vid_publish_date = models.DateField()
    vid_views = models.IntegerField()


class VTubeUser(models.Model):
    usr_id = models.AutoField(primary_key=True)
    usr_username = models.CharField(max_length=25)
    usr_password = models.CharField(max_length=32)
    usr_email = models.EmailField(max_length=50)


class Comment(models.Model):
    cmt_id = models.AutoField(primary_key=True)
    cmt_text = models.TextField()
    cmt_vid_id = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comment') 
    cmt_usr_id = models.ForeignKey(VTubeUser, on_delete=models.CASCADE, related_name='comment') 