# Dados dos vectores A y B de igual cantidad de elementos con números entre 1 y 12 cargados aleatoriamente, obtener el producto escalar: Σ A(i) * B(i). 
import random

vector_a = [0] * 5
vector_b = [0] * 5

# funcion para cargar vectores
def cargarV(vector):
    for i in range(len(vector)):
        vector[i] = random.randint(1,12) 
    return vector
cargarV(vector_a)
# funcion para mostrar el vector
def mostrarV (vector):
    for i in range(len(vector)):
        print(vector[i], end = " ")

mostrarV(vector_a)