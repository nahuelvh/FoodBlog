from django.contrib import admin
from django.urls import path
from AppFoodBlog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home_request, name = "Home"),
    path('accounts/login/', login_request, name = "Login"),
    path('accounts/profile/', Perfil, name = "Profile"),
    path('accounts/profile_update/<user_id>/', editarPerfil, name = "Profile_update"),
    path('accounts/logout/', LogoutView.as_view(template_name='AppFoodBlog/logout.html'), name = "Logout"),
    path('accounts/signup/', register_request, name = "Signup"),
    path('about/', acerca_request, name = "About"),
    path('pages/', pages_list.as_view(), name = "Pages_list"),
    path('pages/<pk>/', pages_detail.as_view(), name = "Pages"),
    path('pages_create/',pagesCreate, name="Pages_create"),
    path('pages_update/<posteo_id>', pagesUpdate, name="Pages_update"),
    path('pages_delete/<pk>', pages_delete.as_view(), name="Pages_delete"),
    path('comentar/', comentario_request, name = "Comentario"),
    path('posteo/', estiloposteo, name = "estiloposteo"),
    path('messages/', listaChats, name = "listaChats"),
    path('messages/<receptor>/', chat, name = "chat"),
]