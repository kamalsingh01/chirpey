from django.db import models
from django.contrib.auth.models import AbstractUser
from user_app.manager import UserManager


# Custom User Model

class UserModel(AbstractUser):
    objects = UserManager()

    id = models.AutoField(primary_key=True, editable=False, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    username = models.CharField(max_length=20, blank=False, unique=True)
    email = models.EmailField(max_length=100, unique=True, blank=False)
    bio = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField()
    profile_image = models.ImageField(upload_to="user/", null=True)

    REQUIRED_FIELDS = ['first_name',
                       'last_name',
                       'email']
    class Meta:
        db_table = "user_tb1"


