# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:47:34 2020

@author: USUARIO
"""
def direccion(calle,sector,codigopostal,referencia,numcasa):
    print('su direccion es ;','sector:',sector,'calle',calle)
    print('su casa es la #;',numcasa,'con codigo postal #:',codigopostal)
    print('y esta cerca de :',referencia)
    
print('ingrese los datos que se solicitan de direccion')
c=input('ingrese la calle')
s=input('ingrese sectorde residencia:')
cod=input('ingrese codigo postal:')
r=input('ingrese una referencia de su domicilio:')
num=input('ingrese el # de casa:')

direccion(c,s,cod,r,num)

