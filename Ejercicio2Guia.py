def ordenar(pila):
    # Creamos una pila auxiliar para ayudar con el orden
    pila_auxiliar = []
    
    # Mientras haya elementos en la pila original
    while pila:
        # Sacamos el elemento de la pila original
        elemento = pila.pop()
        
        # Movemos elementos de la pila auxiliar de vuelta a la pila original si son menores que el actual
        while pila_auxiliar and pila_auxiliar[-1] > elemento:
            pila.append(pila_auxiliar.pop())
        
        # Colocamos el elemento actual en la pila auxiliar
        pila_auxiliar.append(elemento)
    
    # Devolvemos la pila auxiliar, que está ordenada
    return pila_auxiliar

# Ejemplo de uso
pila = [1, 3, 2, 4]
pila_ordenada = ordenar(pila)
print("Pila ordenada:", pila_ordenada)
