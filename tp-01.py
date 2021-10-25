# Dados dos vectores A y B de igual cantidad de elementos con números entre 1 y 12 cargados aleatoriamente, obtener el producto escalar: Σ A(i) * B(i). 
import random
vector_a = [0] * 5
vector_b = [0] * 5

# funcion para cargar vectores
def cargarV(vector):
    for i in range(len(vector)):
        vector[i] = random.randint(1, 10) 
    return vector
cargarV(vector_a)
cargarV(vector_b)

# funcion para mostrar el vector
def mostrarV (vector):
    for i in range(len(vector)):
        print(vector[i], end = " ")
mostrarV(vector_a)
print()
mostrarV(vector_b)
print()
def producto_escalar (v1, v2):
    total = 0
    for i in range(len(v1)):
        total += v1[i] * v2[i]
        print(f'{total}', end= " + ")
        print()
    return print(f'El producto escalar es {total}')

producto_escalar(vector_a, vector_b)

#Dados dos arreglos de 120 elementos cada uno cargados aleatoriamente entre 1 y 1000, hallar la suma de los elementos que ocupan las posiciones pares del primero con los elementos que ocupan las impares del segundo. 

arr1 = [0] * 10
arr2 = [0] * 10

cargarV(arr1)
cargarV(arr2)
mostrarV(arr1)
print()
mostrarV(arr2)
print()

def calcularSumaParImpar(vec1, vec2):
    par = 0
    impar = 0
    for i in range(0, len(vec1), 2):
        par += vec1[i]
    for j in range(1, len(vec2), 2):
        impar += vec2[j]

    total = par + impar
    return total

print(calcularSumaParImpar(arr1, arr2))