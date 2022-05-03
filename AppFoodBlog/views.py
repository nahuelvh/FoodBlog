from asyncio.windows_events import NULL
from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppFoodUsers.forms import RegistroUsuarioForm, UserEditForm
from AppFoodBlog.models import *
from django.views.generic import DetailView, ListView, UpdateView, DeleteView
from AppFoodBlog.forms import *
from AppFoodUsers.models import *
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

            return render(request, "AppFoodBlog/login.html", {'form':form})

    form = AuthenticationForm()

    return render(request, "AppFoodBlog/login.html", {'form':form})

def register_request(request):

    if request.method == "POST":

        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data
            form.save()
            
            user = User.objects.get(username=username['username'])

            usuario = Usuario( user = user, descripcion = username['descripcion'], url = username['url'] )
            usuario.save()

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
    fields = ['titulo', 'subtitulo', 'texto', 'imagen', 'fechaImagen']
    success_url = reverse_lazy('Pages_list')

class pages_delete(DeleteView):

    model = Posteo
    template_name = "AppFoodBlog/pages_delete.html"
    success_url = reverse_lazy('Pages_list')

def pagesCreate(request):
    
    if request.method == 'POST':

        formulario = PagesCreate(request.POST, request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data

            fechaImagen = None

            if data['imagen']:
                fechaImagen = datetime.now()

            posteo = Posteo (user = request.user , titulo = data['titulo'], subtitulo = data['subtitulo'], texto = data['texto'], imagen = data['imagen'], fechaImagen = fechaImagen)

            posteo.save()

            return redirect("Pages", pk=posteo.id)

        else:

            return render(request, "AppFoodBlog/pages_create.html")

    else:

        formulario = PagesCreate()

    return render(request, "AppFoodBlog/pages_create.html", {"formulario": formulario})

def pagesUpdate(request, posteo_id):

    posteo = Posteo.objects.get(id=posteo_id)
    
    if request.method == 'POST':

        formulario = PagesUpdate(request.POST, request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data

            fechaImagen = None

            if not data['imagen'] == posteo.imagen:
                fechaImagen = datetime.now()

            posteo.user = request.user 
            posteo.titulo = data['titulo']
            posteo.subtitulo = data['subtitulo']
            posteo.texto = data['texto']
            posteo.imagen = data['imagen']
            posteo.fechaImagen = fechaImagen

            posteo.save()

            return redirect("Pages", pk=posteo.id)

        else:

            return render(request, "AppFoodBlog/pages_update.html")

    else:

        formulario = PagesUpdate(initial={'user': posteo.user, 'titulo': posteo.titulo, 'subtitulo': posteo.subtitulo, 'texto': posteo.texto, 'imagen': posteo.imagen})

    return render(request, "AppFoodBlog/pages_update.html", {"formulario": formulario, "posteo_id": posteo_id})

def Perfil(request):

    return render (request, "AppFoodBlog/profile.html")

def editarPerfil(request, user_id):

    user = request.user
    
    try:
        usuario = Usuario.objects.get(user_id = user_id)
    except:
        usuario = Usuario(user= user, descripcion = "", url = "", avatar = "")
        usuario.save()

    if request.method == "POST":

        formulario = UserEditForm(request.POST, request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data

            user.email = data['email']
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.password1 = data['password1']
            user.password2 = data['password2']

            user.save()

            usuario.descripcion = data['descripcion']
            usuario.url = data['url']
            usuario.avatar = data['avatar']

            usuario.save()

            return render(request, "AppFoodBlog/home.html")

    else:
        
        formulario = UserEditForm(initial={'username':user.username, 'email':user.email, 'descripcion':usuario.descripcion, 'url':usuario.url, 'first_name':user.first_name, 'last_name':user.last_name, 'avatar':usuario.avatar})

    return render (request, "AppFoodBlog/profile_update.html", {"formulario": formulario, "user": user})


def comentario_request(request):

    if request.method == "POST":

        posteo = Posteo.objects.get(id=int(request.POST['posteo']))
 
        if request.POST['texto'] == "":
            error = "No se puede enviar un mensaje vacío."

        else:    
            comentario = Comentario(user = request.user, posteoId = posteo, texto = request.POST['texto'])
            comentario.save()

        return redirect("Pages", pk=posteo.id)

    return redirect("Pages", pk=posteo.id)

def estiloposteo(request):

    return render(request, "AppFoodBlog/posteo.html")

def listaChats(request):

    if request.method == "GET":

        usuarios = User.objects.all().exclude(id=request.user.id).order_by('username')

        return render(request, "AppFoodBlog/messages.html", {"usuarios": usuarios})

    return render(request, "AppFoodBlog/messages.html")

def chat(request, receptor):

    receptor_id = User.objects.get(username=receptor)
    error = ""
    mensajes = Mensaje.objects.filter(userEmisor__in=[request.user,receptor_id], userReceptor__in=[request.user,receptor_id]).order_by('fechaMensaje')

    if request.method == "POST":

        if request.POST['texto'] == "":
            error = "No se puede enviar un mensaje vacío."
        else:
            mensaje = Mensaje(userEmisor = request.user, userReceptor = receptor_id, texto = request.POST['texto'])
            mensaje.save()

        mensajes = Mensaje.objects.filter(userEmisor__in=[request.user,receptor_id], userReceptor__in=[request.user,receptor_id]).order_by('fechaMensaje')

        return render(request, "AppFoodBlog/messages_chat.html", {"mensajes": mensajes, "receptor": receptor_id, "error": error})
    
    return render(request, "AppFoodBlog/messages_chat.html", {"mensajes": mensajes, "receptor": receptor_id, "error": error})
