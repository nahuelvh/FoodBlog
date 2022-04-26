from cProfile import label
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.

class Posteo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=120)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    subtitulo = models.CharField(max_length=500)
    texto = RichTextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='imagenes/', null=True, blank=True)
    fechaImagen = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user}: {self.titulo}"

class Comentario(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fechaComentario = models.DateTimeField(auto_now_add=True)
    posteoId = models.ForeignKey(Posteo, related_name="comentarios", on_delete=models.CASCADE)
    texto = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.posteoId.titulo} - {self.user}: {self.fechaComentario}"

class Mensaje(models.Model):
    id = models.BigAutoField(primary_key=True)
    userEmisor = models.ForeignKey(User, related_name="emisor", on_delete=models.CASCADE)
    userReceptor = models.ForeignKey(User, related_name="receptor", on_delete=models.CASCADE)
    fechaMensaje = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.userEmisor} a {self.userReceptor}"