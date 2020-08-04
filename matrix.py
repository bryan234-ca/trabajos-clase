# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:34:36 2020

@author: USUARIO
"""
matrix=[[0,0,0,0,0,0],[0,0,0,0,0,0],
        [0,0,0,0,0,0],[0,0,0,0,0,0],
        [0,0,0,0,0,0]]
for i in range (0,5):
    for j in range(0,6):
        print('ingrese el valor para la posicion')
        matrix[i][j]=int(input())
print(matrix) 
