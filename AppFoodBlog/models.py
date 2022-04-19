from cProfile import label
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nick = models.CharField(max_length=40)
    texto = models.CharField(max_length=500)

class Posteo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=120)
    fechaPublicacion = models.DateTimeField(auto_now=True)
    subtitulo = models.CharField(max_length=500)
    texto = RichTextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)

    def __str__(self):
        return f"{self.user}: {self.titulo}"

class Comentario(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fechaComentario = models.DateTimeField(auto_now=True)
    posteoId = models.ForeignKey(Posteo, on_delete=models.CASCADE)
    texto = models.TextField(max_length=300)