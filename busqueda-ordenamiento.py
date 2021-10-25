# Dado un arreglo de N elementos de tipo entero  y un número X ingresado por teclado, escribir un función que:
# Busque todos los elementos que coincidan con X y devuelva la cantidad de coincidencias encontradas.
# Busque la primera coincidencia del elemento en la lista y devuelva su posición. Si X no existe en el arreglo debe devolver -1.
#  Utilizando la función anterior, busque todos los elementos que coincidan con X y devuelva un arreglo con las posiciones que ocupan estos elementos en el arreglo original. Si no hay elementos coincidentes, devolverá un arreglo vacío.

import random
vector = [0] * 10

def carga(vector):
    n = len(vector)
    for i in range(n):
        vector[i] = random.randint(1,10)
        
def muestra(vector):
    n = len(vector)
    for i in range(n):
        print(vector[i], end = " ")   

def buscaElementos(vector, numero):
    long = len(vector)
    coincidencias = 0
    i = 0
    while (i < long):
        if vector[i] == numero:
            coincidencias += 1
        i += 1
    return coincidencias
        
## Prueba ejercicio A
carga (vector)
muestra(vector)
print()
print(f'{buscaElementos(vector, 4)} coincidencias con el numero 4.')
    
         