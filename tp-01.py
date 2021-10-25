# Dados dos vectores A y B de igual cantidad de elementos con números entre 1 y 12 cargados aleatoriamente, obtener el producto escalar: Σ A(i) * B(i). 
import random
vector_a = [0] * 5
vector_b = [0] * 5

# funcion para cargar vectores
def cargarV(vector):
    for i in range(len(vector)):
        vector[i] = random.randint(1, 2) 
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

print()
# Escribir un procedimiento que permita pasar los elementos a la derecha

# Cargar un vector con 50 elementos numéricos y calcular la cantidad de números negativos, positivos y ceros que se encuentran en el vector.  
vector_50e = [0] * 50

def cargaVectorEspecial(vec):
    for i in range(len(vec)):
        vec[i] = random.randint(-100,100)
    return vec

cargaVectorEspecial(vector_50e)
mostrarV(vector_50e)
print() 

def negPosZero(vec):
    pos = 0
    neg = 0
    zero = 0
    for i in range(len(vec)):
        if vec[i] > 0:
            pos += 1
        elif vec[i] < 0:
            neg += 1
        else:
            zero += 1
    print(f'Positivos: {pos}, negativos {neg}, ceros {zero}')

    return pos,neg,zero

negPosZero(vector_50e)





# Ingresar 1000 edades en un vector e indicar cuál es la edad de mayor frecuencia (la que más se repite).  
vector_edades = [0] * 10

cargarV(vector_edades)

def mostrarMasRepite(vector):
    numero_aux = 0
    for i in range(len(vector)):
        print(vector.count(i), end = " ")
        
    return vector[i]





# Realizar una función que determine si dos vectores cargados con números naturales, de igual cantidad de elementos, son idénticos.  
vector_igual1 = [0]*2
vector_igual2 = [0]*2

cargarV(vector_igual1)
cargarV(vector_igual2)
mostrarV(vector_igual1)
print()
mostrarV(vector_igual2)
print()

def verificarIdenticos(vector1, vector2):
    i, n = 0, len(vector_igual1)
    repite = True
    while i < n and repite:
        if vector1[i] == vector2[i]:
            repite = True
            i += 1
        else:
            repite= False
    
    print("IDENTICO") if repite else print("NO SON IDENTICOS")
    
verificarIdenticos(vector_igual1,vector_igual2)





# Escribir un procedimiento que acepte como parámetro un vector que contiene números positivos, que puede contener valores duplicados, y reemplace cada elemento repetido por -1 (menos uno).  El procedimiento debe retornar el vector modificado y la cantidad de veces que fue modificado.  

def vectorModificado(vector):
    new_vec = []
    for i in range(len(vector)):
        if i not in new_vec:
            vector[i] = -1
            new_vec += i
    return vector, new_vec        
    
    

print(vectorModificado(vector_igual2))

        