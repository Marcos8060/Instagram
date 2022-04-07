from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pictures',null=False)
    title = models.CharField(max_length=30)
    caption = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User,related_name='liked',default=None,blank=True)

    def __str__(self):
        return self.title
