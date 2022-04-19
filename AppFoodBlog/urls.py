from django.contrib import admin
from django.urls import path
from AppFoodBlog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home_request, name = "Home"),
    path('accounts/login/', login_request, name = "Login"),
    path('accounts/profile_update/<user_id>/', editarperfil, name = "Profile"),
    path('accounts/logout/', LogoutView.as_view(template_name='AppFoodBlog/logout.html'), name = "Logout"),
    path('accounts/signup/', register_request, name = "Signup"),
    path('accounts/about/', acerca_request, name = "About"),
    path('accounts/pages/', pages_list.as_view(), name = "Pages_list"),
    path('accounts/pages/<pk>/', pages_detail.as_view(), name = "Pages"),
    path('accounts/pages_create/',pagesCreate, name="Pages_create"),
    path('accounts/pages_update/<pk>',pages_update.as_view(), name="Pages_update"),
    path('accounts/pages_delete/<pk>',pages_delete.as_view(), name="Pages_delete"),
]