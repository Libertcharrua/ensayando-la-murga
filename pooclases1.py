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
    #Atributos de clase. común a todos los objetos del tipo perro
    especie = "mamífero"
    #El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):
        print(f"""Creando perro {nombre}{raza}""")
        
        #Atributos de instancia pertenecen al objeto en específico
        self.nombre = nombre
        self.raza = raza
    
    def ladra(self):
        print("Guau")

    def caminar(self,pasos):
        print(f"""Caminando {pasos} pasos""")

#Creando un objeto de la clase perro
mi_perro = perro("Luna", " callejero")
#Y usando sus métodos
mi_perro.ladra()
mi_perro.caminar(15)
print(type(mi_perro))


#Accediendo a atributos concretos 
print(mi_perro.nombre)
print(mi_perro.raza)
print(mi_perro.especie)
print(f"""Ya que es un atributo de clase no es necesario
      invocar al objeto mi_perro {perro.especie}""")