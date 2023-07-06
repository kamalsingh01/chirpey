from django.db import models
from user_app.models import UserModel


class Post(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    content = models.CharField(max_length=250, editable=True)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='post/', null=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

    objects = models.manager


class Comment(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    content = models.CharField(max_length=100, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    objects = models.manager


class Like(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    # one user can only like one post once
    class Meta:
        unique_together = ('user', 'post')

    object = models.Manager
