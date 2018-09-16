from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_trainer = models.BooleanField(default=False)
    is_client= models.BooleanField(default=False)


class TrainerProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    age = models.IntegerField(null=True)
    location = models.CharField(max_length=30,null=True)
    skills = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.user.username


class ClientProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    age = models.IntegerField(null=True)
    location = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.user.username
