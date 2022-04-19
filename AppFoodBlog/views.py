from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppFoodUsers.forms import RegistroUsuarioForm, UserEditForm
from AppFoodBlog.models import Posteo
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from AppFoodBlog.forms import PagesCreate
from django.urls import reverse_lazy

# Create your views here.

def home_request(request):

    return render(request, "AppFoodBlog/home.html")

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppFoodBlog/home.html")

            else:
                return render(request, "AppFoodBlog/home.html")
            
        else:
            return render(request, "AppFoodBlog/home.html")

    form = AuthenticationForm()

    return render(request, "AppFoodBlog/login.html", {'form':form})

def register_request(request):

    if request.method == "POST":

        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "AppFoodBlog/home.html")

    else:
        form = RegistroUsuarioForm()

    return render(request, "AppFoodBlog/signup.html", {"form":form})

def acerca_request(request):

    return render(request, "AppFoodBlog/about.html")


class pages_list(ListView):

    model = Posteo
    template_name = "AppFoodBlog/pages_list.html"

class pages_detail(DetailView):

    model = Posteo
    template_name = "AppFoodBlog/pages_detail.html"

class pages_update(UpdateView):

    model = Posteo
    template_name = "AppFoodBlog/pages_update.html"
    fields = ['titulo', 'subtitulo', 'texto', 'imagen']

class pages_delete(DeleteView):

    model = Posteo
    template_name = "AppFoodBlog/pages_delete.html"
    success_url = reverse_lazy('Home')



def pagesCreate(request):
    
    if request.method == 'POST':

        formulario = PagesCreate(request.POST, request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data

            posteo = Posteo (user = request.user , titulo = data['titulo'], subtitulo = data['subtitulo'], texto = data['texto'], imagen = data['imagen'])

            posteo.save()

            return render(request, "AppFoodBlog/pages_list.html")

        else:

            return render(request, "AppFoodBlog/pages_create.html")

    else:

        formulario = PagesCreate()

    return render(request, "AppFoodBlog/pages_create.html", {"formulario": formulario})

def editarperfil(request, user_id):

    usuario = request.user

    if request.method == "POST":

        formulario = UserEditForm(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            usuario.email = data['email']
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']
            usuario.password1 = data['password1']
            usuario.password2 = data['password2']

            usuario.save()

            return render(request, "AppFoodBlog/home.html")

    else:
        
        formulario = UserEditForm(initial={'email':usuario.email, 'first_name':usuario.first_name, 'last_name':usuario.last_name})

    return render (request, "AppFoodBlog/profile_update.html", {"formulario": formulario, "usuario": usuario})