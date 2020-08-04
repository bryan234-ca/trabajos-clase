# -*- un año y un  mes -*-
"""
Created on Tue Jul  7 22:50:39 2020

@author: Bryan carpio
"""
def cantidad_dias(mes):
    if mes.lower()in('enero','marzo','julio','agosto','octubre','diciembre'):
        return '31'
    elif mes.lower() == 'febrero':
        return '28'
    else:
        return '30'
    
 
nombre_mes = input('ingrese el nombre del mes:')
 
print(cantidad_dias(nombre_mes))
    
    

