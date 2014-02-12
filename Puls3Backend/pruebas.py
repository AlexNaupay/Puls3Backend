import os
import django

#Ruta de la carpeta del proyecto
ruta = os.path.dirname(os.path.realpath(__file__))

#Lo mismo que ruta
ruta2 = os.path.realpath(os.path.dirname(__file__))

#
ruta3 = os.path.realpath(os.path.realpath(__file__))
print(ruta)
print(ruta2)
print(ruta3)

print("------------------------------")
print(os.path.realpath(__file__))
print(os.path.dirname(__file__))
print(__file__)