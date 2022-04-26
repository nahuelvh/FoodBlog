from django.contrib import admin
from AppFoodBlog.models import *
from AppFoodUsers.models import *

# Register your models here.

admin.site.register(Posteo)
admin.site.register(Comentario)
admin.site.register(Usuario)
admin.site.register(Mensaje)