import random

# funcion para mostrar matriz
def mostrar(matriz, c, f):
    for i in range(f):
        for j in range(c):
            print(matriz[i][j], end = " ")
        print(" ")
    print("")

# declaramos cantidad de filas y de columnas

filas = 3
columnas = 3

# inicializamos la matriz en cero

matriz = [[0] * columnas for i in range(filas)]

#cargamos la matriz con numeros aleatorios

for i in range(filas):
    for j in range(columnas):
        matriz[i][j] = random.randint(1,10)






# Dada una matriz de 3 filas por 4 columnas, calcular la sumatoria de sus elementos:  ΣM(i,j)

f = 3
c = 4
matriz1 = [[0] * c for i in range(f)]
for i in range(f):
    for j in range(c):
        matriz1[i][j] = random.randint(1,3)

def sumatoria_matriz(m, c, f):
    total = 0
    for i in range(f):
        for j in range(c):
            total += m[i][j]

    return total

print(f'El total de la sumatoria de la matriz {matriz1} es {sumatoria_matriz(matriz1, c, f)}')
print()

# Leer una matriz de tres filas por tres columnas y calcular la suma de cada una de sus filas y de sus columnas, colocando los resultados en dos vectores, uno para la suma de las filas y otro para la suma de las columnas

fila_ej2 = 3
colu_ej2 = 3
matriz_ej2 = [[0] * colu_ej2 for i in range(fila_ej2)]
for i in range(fila_ej2):
    for j in range(colu_ej2):

        matriz_ej2[i][j] = random.randint(1,5)
vector_filas = [0] * 3
vector_colum = [0] * 3

mostrar(matriz_ej2, colu_ej2, fila_ej2)
def suma_vector(matriz,filas,columnas,v1,v2):
    for i in range(filas):
        v1[i] = matriz[i]


    colList = []
    i = 0
    for fila in range(filas):
        for col in range(columnas):
            colList = matriz[fila[col]]

  
    return v1, colList
print(suma_vector(matriz_ej2,fila_ej2, colu_ej2,vector_filas, vector_colum))