from django.shortcuts import render
from MiApp.models import Jugadores, Torneos, Entrenadores, Avatar, Blogs
from .forms import CrearJugadorForm, CrearEntrenadorForm, CrearTorneosForm, SignUpForm, UserEditForm, CrearBlogsForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import datetime
now = datetime.now()



# Create your views here.
#@login_required
def inicio(request):
    if request.user.is_authenticated:
        
        imagenes = Avatar.objects.filter(user=request.user.id)
        try:
            return render(request, 'MiApp/index2.html', {'url': imagenes[0].imagen.url})
        except:
            return render(request, 'MiApp/index2.html')
    else:
        return render(request, 'MiApp/index2.html')

def mostrar_jugadores(request):
    j1 = Jugadores(nombre="Rafael",apellido="Gonzalez", edad = 36, nacionalidad = "Espania" )
    j2 = Jugadores(nombre="Miguel",apellido="Juarez", edad = 40, nacionalidad = "Argentina" )
    j1.save()
    j2.save()
    return render (request, 'MiApp/jugadores.html' , {'jugadores': [j1 , j2]})


def mostrar_torneos(request):
    t1 = Torneos(nombre="French Open", pais="Francia", puntos_otorgados = 2000)
    t1.save()
    t2 = Torneos(nombre="US Open", pais="USA", puntos_otorgados = 1500)
    t2.save()
    return render (request, 'MiApp/torneos.html' , {'torneos': [t1, t2]})


def mostrar_entrenadores(request):
    e1 = Entrenadores(nombre="Carlos",apellido="Alberdi", entrenado = "Rafeal Gonzalez", email = "cmoya@hotmail.com" )
    e2 = Entrenadores(nombre="Juan",apellido="Garcia", entrenado = "Ramiro Alvarez", email = "jg@hotmail.com" )
    e1.save()
    e2.save()
    return render (request, 'MiApp/entrenadores.html' , {'entrenadores': [e1, e2]})

def mostrar_jugadores_pagina(request):
    return render(request, 'MiApp/jugadores.html')

def pages(request):
        return render(request, 'MiApp/pages.html')

def no_hay_info(request):
        return render(request, 'MiApp/no_hay_mas_info.html')

@login_required
def formulario_jugadores(request):
    if request.method == 'POST':
        formulario = CrearJugadorForm(request.POST)

        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            jugador = Jugadores(nombre = formulario_limpio["nombre"], apellido = formulario_limpio["apellido"], edad = formulario_limpio["edad"], nacionalidad = formulario_limpio["nacionalidad"])
            jugador.save()
            return render(request, 'MiApp/index2.html')
    else:
        formulario = CrearJugadorForm()

    return render(request, 'MiApp/crear_jugador.html', {'formulario': formulario})





@login_required
def formulario_entrenadores(request):
    if request.method == 'POST':
        formulario = CrearEntrenadorForm(request.POST)

        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            entrenador = Entrenadores(nombre = formulario_limpio["nombre"], apellido = formulario_limpio["apellido"], entrenado = formulario_limpio["entrenado"], email = formulario_limpio["email"])
            entrenador.save()
            return render(request, 'MiApp/index2.html')
    else:
        formulario = CrearEntrenadorForm()

    return render(request, 'MiApp/crear_entrenador.html', {'formulario': formulario})

@login_required
def formulario_torneos(request):
    if request.method == 'POST':
        formulario = CrearTorneosForm(request.POST)

        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            torneo = Torneos(nombre = formulario_limpio["nombre"], pais = formulario_limpio["pais"], puntos_otorgados = formulario_limpio["puntos_otorgados"])
            torneo.save()
            return render(request, 'MiApp/index2.html')
    else:
        formulario = CrearTorneosForm()

    return render(request, 'MiApp/crear_torneo.html', {'formulario': formulario})

def buscar_jugador(request):
    
    if request.GET.get('apellido', False):
        apellido = request.GET["apellido"]
        jugador = Jugadores.objects.filter(apellido__icontains=apellido)
        return render(request, 'MiApp/buscar_jugador.html', {'jugadores': jugador})

    else:
        respuesta = "No hay datos"
    return render(request, 'MiApp/buscar_jugador.html', {'respuesta': respuesta})

def mostrar_jugadores_todos(request):
    jugadores = Jugadores.objects.all()
    context = {'jugadores': jugadores}
    return render(request,'MiApp/mostrar_jugadores.html', context=context)

def mostrar_entrenadores_todos(request):
    entrenadores = Entrenadores.objects.all()
    context = {'entrenadores': entrenadores}
    return render(request,'MiApp/entrenadores.html', context=context)


def mostrar_torneos_todos(request):
    torneos = Torneos.objects.all()
    context = {'torneos': torneos}
    return render(request,'MiApp/torneos.html', context=context)

def eliminar_jugador(request, apellido):
    jugadores = Jugadores.objects.get(apellido=apellido)
    jugadores.delete()
    jugadores = Jugadores.objects.all()
    context = {'jugadores': jugadores}
    return render(request,'MiApp/mostrar_jugadores.html', context=context)


def actualizar_jugadores(request, jugador_id):
    jugador = Jugadores.objects.get(id=jugador_id)
    
    if request.method == 'POST':
        formulario = CrearJugadorForm(request.POST)

        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data
            jugador.nombre = formulario_limpio['nombre']
            jugador.apellido = formulario_limpio['apellido']
            jugador.edad = formulario_limpio['edad']
            jugador.nacionalidad = formulario_limpio['nacionalidad']
            jugador.save()
            return render(request, 'MiApp/index2.html')
    else:
        formulario = CrearJugadorForm(initial={'nombre':jugador.nombre,'apellido':jugador.apellido,'edad':jugador.edad,'nacionalidad':jugador.nacionalidad})

    return render(request, 'MiApp/modificar_jugador.html', {'formulario': formulario})


def editar_usuario(request):
    if request.user.is_authenticated:
        usuario = request.user
        if request.method == 'POST':
            usuario_form = UserEditForm(request.POST)

            if usuario_form.is_valid():
                informacion = usuario_form.cleaned_data
                usuario.username = informacion['username']
                usuario.email = informacion['email']
                usuario.password1 = informacion['password1']
                usuario.password2 = informacion['password2']
                usuario.save()

                return render(request,'MiApp/index2.html')
        
        else:
            usuario_form = UserEditForm(initial={
                'username': usuario.username,
                'email': usuario.email,
            }) 
        
        return render(request,'MiApp/MiApp/admin_update.html', {
            'form':  usuario_form,
            'usuario': usuario
            })
    else:
        return render(request, 'MiApp/index2.html')





class JugadoresList(ListView):

    model = Jugadores
    template_name = 'MiApp/MiApp/jugadores_list.html'





class JugadoresDetailView(LoginRequiredMixin, DetailView):

    model = Jugadores
    template_name = 'MiApp/MiApp/jugadores_detalle.html'

class JugadoresDeleteView(LoginRequiredMixin, DeleteView):
    model = Jugadores
    success_url = reverse_lazy('List')

class JugadoresUpdateView(LoginRequiredMixin, UpdateView):
    model = Jugadores
    success_url = reverse_lazy('List')
    fields = ['nombre' , 'apellido']

class JugadoresCreateView(LoginRequiredMixin, CreateView):
    model = Jugadores
    success_url = reverse_lazy('List')
    fields = ['nombre' , 'apellido', 'edad', 'nacionalidad']


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('Inicio')
    template_name = 'MiApp/registro.html'

class AdminLoginView(LoginView):
    template_name = 'MiApp/login.html'


class AdminLogoutView(LogoutView):
    template_name = 'MiApp/logout.html'


class BlogsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Blogs
    success_url = reverse_lazy('NuevosBlogs')
    fields = ['titulo' , 'subtitulo', 'autor', 'cuerpo', 'imagen']


class BlogsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser
    model = Blogs
    success_url = reverse_lazy('NuevosBlogs')

@login_required
def formulario_blogs(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            formulario = CrearBlogsForm(request.POST, request.FILES)

            if formulario.is_valid():
                formulario_limpio = formulario.cleaned_data
                blog = Blogs(titulo = formulario_limpio["titulo"], subtitulo = formulario_limpio["subtitulo"], autor = formulario_limpio["autor"], cuerpo = formulario_limpio["cuerpo"], fecha_imagen = str(now.year)+"-"+str(now.month)+"-"+str(now.day), imagen = formulario_limpio["imagen"]) #formulario_limpio["fecha_imagen"])#, imagen = formulario.cleaned_data["imagen"], cuerpo = formulario_limpio["cuerpo"])
                blog.save()
                return render(request, 'MiApp/mostrar_nuevos_blogs.html')
        else:
            formulario = CrearBlogsForm()

        return render(request, 'MiApp/crear_blog.html', {'formulario': formulario})
    else:
        return render(request, 'MiApp/login.html')

def mostrar_nuevos_blogs(request):
    blog = Blogs.objects.all()
    context = {'blog': blog}
    if len(blog) == 0:
        return render(request,'MiApp/no_hay_publicaciones.html', context=context)
    else:
        return render(request,'MiApp/mostrar_nuevos_blogs.html', context=context)
    

def about_me(request):

    return render(request,'MiApp/about_me.html')
    
