from rest_framework import serializers
from main.models import Post
from main.models import Categoria


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('url', 'titulo', 'enlace', 'categoria', 'autor', 'fecha_publicacion', 'votos',)


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('url', 'nombre',)
