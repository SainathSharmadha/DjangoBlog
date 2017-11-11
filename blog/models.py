from django.db import models
from django.utils import timezone
from .validators import validate_file_extension
# Create your models here.

class UserComment(models.Model):
    user = models.CharField(max_length=200,null=True)
    comment = models.TextField(null=True)
    def set(self,user,comment):
        self.user = user
        self.comment = comment


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    picture = models.ImageField(validators=[validate_file_extension])
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)
    user_comments = []

    def add_Comment(self,user,comment):
        userComment = UserComment()
        self.user_comments.append(userComment.set(user,comment))

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title





