#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 13:56:17 2024

@author: libert-argenta
"""
'''POO en python
1 ) Creando clases vacias'''

#Creando una clase vacia
class perro:
    
    #El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):
        print(f"""Creando perro {nombre}{raza}""")
        
        #Atributos de instancia
        self.nombre = nombre
        self.raza = raza
    

#Creando un objeto de la clase perro
mi_perro = perro("Luna", " callejero")
print(type(mi_perro))