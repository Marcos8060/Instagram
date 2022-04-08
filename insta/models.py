from django.db import models
from django.contrib.auth.models import User

# post model

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_pictures',null=False)
    title = models.CharField(max_length=30)
    caption = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User,related_name='liked',default=None,blank=True)

    def __str__(self):
        return self.title

# comment model
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.post.title


