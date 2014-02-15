# -*- encoding: utf-8 -*-
from random import choice
from main.models import Categoria
from django.core.cache import cache #para hacer el cache
def frase_footer(request):
	numero = cache.get('numero')
	if numero is None: #Si aún no hay numero guardado
		numero = choice(('1','2','3','4','5'))
		cache.set('numero',numero)
	return {'frase':'Sueña, tus sueños crearán la realidad '+numero}

def menu(request):
	categorias=Categoria.objects.all()
	menu={'menu':[]}
	for categoria in categorias:
		menu['menu'].append({'name':categoria.nombre,'url':'/categoria/'+str(categoria.pk)})

	for item in menu['menu']:
		if item['url'] == request.path:
			item['active']=True
	return menu