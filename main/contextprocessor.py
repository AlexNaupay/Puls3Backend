# -*- encoding: utf-8 -*-

from main.models import Categoria

def frase_footer(request):
	return {'frase':'Sueña, tus sueños crearán la realidad'}

def menu(request):
	categorias=Categoria.objects.all()
	menu={'menu':[]}
	for categoria in categorias:
		menu['menu'].append({'name':categoria.nombre,'url':'/categoria/'+str(categoria.pk)})

	for item in menu['menu']:
		if item['url'] == request.path:
			item['active']=True
	return menu