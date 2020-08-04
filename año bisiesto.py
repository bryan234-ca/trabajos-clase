# -*- El año es bisiesto o no -*-
"""
Created on Thu Jul  2 14:29:08 2020

@author: Bryan Carpio
"""
def es_bisiesto(anio):
    if anio % 400 ==0:
        return True
    elif anio % 100 ==0:
        return False
    elif anio % 4 ==0:
        return True
    else:
        return False
               
anio = 1900  
print('¿El año %i es bisiesto?: %s'%(anio,es_bisiesto(anio)))
anio = 2000      
print('¿El año %i es bisiesto?: %s'%(anio,es_bisiesto(anio)))
anio = 2016
print('¿El año %i es bisiesto?: %s'%(anio,es_bisiesto(anio)))
anio = 1987
print('¿El año %i es bisiesto?: %s'%(anio,es_bisiesto(anio)))