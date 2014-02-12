from django.contrib import admin
from main.models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('titulo','categoria','autor','votos_imagen_html')
	list_filter = ('categoria','autor')
	search_fields = ('titulo','autor','categoria__nombre')
	list_editable = ('autor','categoria')

	def votos_imagen_html(self,objeto_render):
		url = objeto_render.votos_en_imagen()
		img = '<img src="%s"/>'%url
		return img
	votos_imagen_html.allow_tags=True #Permitirme html
	votos_imagen_html.admin_order_field='votos'#como ordenar

admin.site.register(Categoria)
admin.site.register(Post,PostAdmin)