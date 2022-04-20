# Se puede definir números como cadenas
from tkinter import N


numero1 = "100" #str
numero2 = "3.14159" #str
print( type(numero1), type (numero2) )

#Para convertir a entero
entero = int(numero1)
print(type (entero) )

#Para convertir a float
flotante = float(numero2)
print(type (flotante) )

#Convertir de número a cadena
num = 300
cadena = str (num)
print( type(cadena))

#leyendo una cadena
nombre = input("Dame tu nombre: ")
print( nombre,type(nombre))

#leyendo un entero
edad = input ("Dame tu edad: ")
edad_int = int(edad)
print( edad_int, type(edad_int))