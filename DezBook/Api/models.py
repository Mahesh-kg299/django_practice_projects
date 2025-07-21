from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=6, primary_key=True)
    username= models.TextField(max_length=25, unique=True)
    first_name= models.TextField(max_length=25)              
    last_name = models.TextField(max_length=25)
    dob= models.DateField()
    email = models.EmailField()

class Post(models.Model):
    post_id = models.CharField(max_length=6, primary_key=True)
    media = models.ImageField()
    caption = models.TextField(max_length=100)
    likes_count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

class Like(models.Model):
    like_id = models.CharField(max_length=6, primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")