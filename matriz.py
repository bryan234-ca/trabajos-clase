# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:48:08 2020

@author: USUARIO
"""
matriz = []

Filas = int(raw_input('cantidad de filas: '))
columnas = int(raw_input('cantidad de columnas: '))

for i in range(filas) :
    matriz.append([0]*columnas)
for f in range(filas):
  for c in range(columnas):
    matriz[f][c] = int(raw_input('elemento %d,%%d :'%(f,c)))
    
print matriz

