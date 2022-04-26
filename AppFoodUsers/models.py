from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Usuario(models.Model):
    user = models.OneToOneField(User, related_name="usuario", on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=120, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)