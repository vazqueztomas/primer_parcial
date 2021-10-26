import random

# Escribir una función que reciba un arreglo de strings e indique si se encuentran ordenados de menor a mayor o no

vecA = ["casa", "auto", "jardin"," terraza", "patio", "garage"]
vecB = ["auto", "casa", "garage","jardin", "patio", "terraza"]

def ordenarVector(vector):
    i = 0
    n = len(vector)
    coincidencia = 0
    for i in range(n):
        for j in range(1, n - i - 1):
            if vector[j] > vector[j + 1]:
                aux = vector[j+1]
                vector[j] = vector [j+1]
                vector[j + 1] = aux
                coincidencia += 1
    
    if coincidencia == 0:
        print('Esta ordenado')
    else:
        print('Estaba desordenado')

ordenarVector(vecA)
ordenarVector(vecB)


# Dados dos arreglos ordenados: A(n) y B(m), construir un nuevo arreglo C que contenga los elementos de A y de B de tal forma que quede también ordenado. Si existen elementos repetidos en los arreglos originales, en C deberán aparecer solamente una vez.

vector_A = [0] * 10
vector_B = [0] * 10

def cargar (vector):
    for i in range(len(vector)):
        vector[i] = random.randint(1,10)

cargar(vector_A)
cargar(vector_B)

def generaVector(v1, v2):
    vector_c = [0] * 10
    for i in range(len(v1)):
        if v1[i] != vector_c[i]:
            vector_c = v1[i]

    for i in range(len(v2)):
        if v2[i] != vector_c[i]:
            vector_c[i] = v2[i]
    
    return vector_c

print(generaVector(vector_A, vector_B))
