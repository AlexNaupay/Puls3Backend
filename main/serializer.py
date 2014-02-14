from rest_framework import serializers
from main.models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Post
		fields = ('url','titulo','enlace','autor','fecha_publicacion','votos',)
