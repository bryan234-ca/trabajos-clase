# -*- La funcion Input -*-
# Sirve para captar la entrada de datos
"""
Created on Fri Jun 19 16:25:13 2020

@author: Bryan Carpio
"""

print ('Ingresa tu nombre')
nom = input()
edad = int(input('ingresa tu edad'))
if edad < 18:
    print('menor de edad')
else:
    print('mayor de edad')
print ('ingresa tu ubicacion')
ubicacion = input()
print ('Tu nombre es:',nom)
print ('Tu edad es:',(edad ))
print ('Tu ubicacion es:',(ubicacion))