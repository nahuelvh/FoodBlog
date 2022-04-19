from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# class Mensaje(models.Model):
#     id = models.BigAutoField(primary_key=True)
#     userEmisor = models.ForeignKey(User, on_delete=models.CASCADE)
#     userReceptor = models.ForeignKey(User, on_delete=models.CASCADE)
#     fechaEnvio = models.DateTimeField(auto_now=True)
#     texto = models.TextField()