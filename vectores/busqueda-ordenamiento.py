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
    i = 0
    n = len(vector)
    coincidencia = 0
    # Para devolver coincidencia
    while (i < n):        
        if vector[i] == numero:
            coincidencia += 1        
        i += 1
    
    encontrado = True
    posi = 0
    while (i < n and encontrado):        
        if vector[i] == numero:
            posi = vector[i]
            encontrado = False
     
    return coincidencia, posi       

## Prueba ejercicio A
# carga (vector)
# muestra(vector)
# print()
# print(f'{buscaElementos(vector, 4)} coincidencias con el numero 4.')

#Realizar un programa que permita, a través de un módulo (función o procedimiento) 
#ordenar un arreglo de 20 elementos. Este módulo recibirá dos parámetros : 
#el primero indicará arreglo a ordenar, y el segundo indicará si el orden será “A” - Ascendente (de menor a mayor) 
#o “D” Descendente (de mayor a menor)

def arreglar_array(vect, orden):
    n = len(vect)
    #vector a ordenar por bubblesort
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if vect[j] > vect[j + 1]:
                temp = vect[j]
                vect[j] = vect[j + 1]
                vect[j + 1] = temp
            
   
    
    # direccion del orden
    if orden == 'a' or orden == 'A':
        return vect
    elif orden == 'D' or orden == 'd':
        return vect[::-1]
    
    
muestra(vector)
print()
print(f'vector ascendiente = {arreglar_array(vector, "A")}')
print(f'vector descendiente = {arreglar_array(vector, "D")}')

# Escribir una función que reciba una lista ordenada y un elemento. Si el elemento se encuentra en la lista, debe encontrar su posición mediante búsqueda binaria y devolverlo. Si no se encuentra, debe agregarlo a la lista en la posición correcta y devolver esa nueva posición.

def busquedaBinaria(vector, elem):
    i = 0
    leng = (len(vector))
    med = 0

    while (i <= leng):
        med = (i + leng) // 2
        if vector[i] < elem:
            i = med + 1
        elif (vector[i] > elem):
            leng = med - 1
        else:
            return med
    return -1


