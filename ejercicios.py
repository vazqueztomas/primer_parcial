import numpy as np

m1 = np.array([0]*10)  # matriz creada con numpy, una sola dimension
m2 = np.array([[0]*10]*4)    # matriz de dos dimensiones, con 10 columnas y 4 filas.
m3 = np.array([[[0]*10]*4]*2)  # matriz de tres dimensiones, con 10 columnas y 4 filas


# para mostrar una matriz, funcion

def mostrarMatriz (m, f, c):
    for fila in range(f):
        for columna in range(c):
            print(m[fila][columna], end= " ")
        print()
    print()
    
mostrarMatriz(m2, 4, 10)
        
