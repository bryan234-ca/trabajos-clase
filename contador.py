# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:44:08 2020

@author: USUARIO
"""


def contar_digitos_letras(cadena):
    digitos = 0
    letras = 0
    
    for c in cadena:
        if c.isdigit():
            digitos += 1
        elif c.isalpha():
            letras += 1
        else:
            pass
    return digitos, letras



texto= input('digite un texto')
resultado = contar_digitos_letras(texto)

print('cantidad de digitos:%i'% resultado[0])
print('cantidad de letras:%i'% resultado[1])

