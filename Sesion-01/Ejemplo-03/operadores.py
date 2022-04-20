# Vamos a ver como se comportan algunos operadores en Python
# usando las siguientes variables

from __future__ import division


operando1 = 6
operando2  = 10
incremento = 0

# Operadores aritmeticos
suma = operando1 + operando2
print( "La suma de los valores es: ")
print(suma)

producto = operando1 * operando2
print( "El resultado de la multiplicación es: ")
print(producto)

division = operando1 / operando2
print( "El resultado de la division es: ")
print(division)

incremento += 1 #incremento = incremento + 1 -> 1
incremento += 2 #incremento = incremento + 2 -> 3
incremento = 5
print("El incremento es:")
print(incremento)

#Operadores lógicos
operando3 = True
operando4 = False

compuerta_and = operando3 and operando4
print("El resultado de la AND es:")
print(compuerta_and)

negando = not operando3
print("Esto es una negación:")
print(negando)