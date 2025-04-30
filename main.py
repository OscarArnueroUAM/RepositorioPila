from classPila import Pila
from separarParImpar import separarParImpar

#Ingreso de datos

pila = Pila()
n = int(input("Ingrese la cantidad de elementos en la pila: "))
for i in range(n):
    elemento = int(input(f"Ingrese el elemento {i+1}: "))
    pila.apilar(elemento)
print("Pila original:", pila)
pila_separada = separarParImpar(pila)
print("Pila separada (pares abajo, impares arriba):", pila_separada)