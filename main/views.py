# -*- encoding:utf:8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from main.models import *
from main.forms import *
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse
from django.core.cache import cache
from django.db.models.signals import post_save  # Envia señal de guardado
from django.contrib.sessions.models import Session  # Borrar cache != de Session
from django.dispatch import receiver
from django.views.generic import ListView
from django.views.generic import DetailView
from rest_framework import viewsets
from main.serializer import PostSerializer
from main.serializer import CategoriaSerializer
from django.views.decorators.cache import cache_page


@receiver(post_save)
def clear_cache(sender, **kwargs):
    if sender != Session:
        cache.clear()


# @cache_page(600) #Tiempo en segundos # No es vale si trabajamos con usuarios
def home(request):
    # if request.method=='POST': #Si viene de clicar en boton de formulario
    if request.POST:
        formulario = PostForm(request.POST)
        if formulario.is_valid():
            post = formulario.save(commit=False)  # Retorna el objeto guardado
            post.autor = request.user
            post.save()
            return HttpResponseRedirect('/')
    else:  # Si estamos en home de llegada
        categorias = Categoria.objects.all()
        posts = Post.objects.order_by('-votos').all()
        formulario = PostForm()
    return render_to_response('index.html', context_instance=RequestContext(request, locals()))


def categoria(request, id_categoria):
    categorias = Categoria.objects.all()
    posts = Post.objects.filter(categoria=id_categoria)
    return render_to_response('index.html', {'categorias': categorias, 'posts': posts},
                              context_instance=RequestContext(request))


@login_required
def up(request, id_post):
    post = Post.objects.get(pk=id_post)
    post.votos = post.votos + 1
    # post.votos+=+1 #Da problemas y de redireccion tambien
    post.save()
    return HttpResponseRedirect('/')


@login_required
def down(request, id_post):
    post = Post.objects.get(pk=id_post)
    post.votos = post.votos - 1
    # post.votos+=-1 #Da problemas y de redireccion tambien
    post.save()
    return HttpResponseRedirect('/')


class HomeListView(ListView):  # ListView, para listas objetos
    model = Post  # El modelo (se tomará todos de la base de datos)
    context_object_name = 'posts'  # Nombre en el contexto (en la plantilla)

    # template_name='index.html'
    def get_template_names(self):  # Nombre de la plantilla
        return 'index.html'


class PostDetailView(DetailView):
    model = Post  # Me pregunto ¿Cómo sabrá que nombre tomar en la plantilla?, pero puse post y tomó eso
    template_name = 'postdetail.html'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()  # La consulta
    serializer_class = PostSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()  # la consulta, automaticamente mostrará la categoria de el
    serializer_class = CategoriaSerializer  # Clase Serializadora
