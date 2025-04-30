'''Implementa un método que reciba una pila de enteros 
como único parámetro. Este método llamado “separarParImpar”
 deberá retornar la pila con los números pares en la parte 
 inferior y los impares en la superior.
 Ejemplo:
Entrada –> [ 2, 3, 6, 8, 11, 13, 18, 21]
Salida –> [ 2, 6, 8, 18, 3, 11, 13, 21] PARES / IMPARES
 Nota: No hace falta que los números estén ordenados de 
menor a mayor, esto solo es un ejemplo. Lo importante es 
separar los pares de los impares.
'''

from classPila import Pila

def separarParImpar(pila):
    if pila.esta_vacia():
        return pila

    # Crear pilas temporales para pares e impares
    pila_pares = Pila()
    pila_impares = Pila()

    # Desapilar elementos y separarlos en pares e impares
    while not pila.esta_vacia():
        elemento = pila.desapilar()
        if elemento % 2 == 0:
            pila_pares.apilar(elemento)
        else:
            pila_impares.apilar(elemento)

    # Volver a apilar los elementos, primero los pares y luego los impares
    while not pila_pares.esta_vacia():
        pila.apilar(pila_pares.desapilar())

    while not pila_impares.esta_vacia():
        pila.apilar(pila_impares.desapilar())

    return pila

