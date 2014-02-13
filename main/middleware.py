
from random import choice
from django.shortcuts import redirect
paises = ['Peru','Mexico','colombia']

def ubicar_pais():
	return choice(paises)

class PaisMiddleware():
	def process_request(self, request):
		pass
	# 	pais = ubicar_pais()
	# 	if pais == "Peru":
	# 		return redirect('http://alexnaupay.hol.es')
	# 	else:
	# 		pass