#Function Description
#Complete the matrixRotation function in the editor below.
#matrixRotation has the following parameter(s):
#int matrix[m][n]: a 2D array of integers
#int r: the rotation factor

#Link: https://www.hackerrank.com/challenges/matrix-rotation-algo/problem?isFullScreen=true

def matriz_vacia(matrix):
    aux = []
    for i in range(len(matrix)):
        aux.append([0] * len(matrix[i]))
    return aux

def rotacion(aux):
    filas = len(aux)
    columnas = len(aux[0])
    cambio = 0
    for i in range(filas):
        pass

def matrixRotation(matrix, r):
    contador = 0
    n = 0
    m = len(matrix[0])-1
    
    matrices = []
    
    aux = matriz_vacia(matrix)

    aux[0] = matrix[0]
    for c in range(2):
        n = 0
        for i in matrix:
            for j in i:
                if contador == 0:
                    pass
    #                print(str(j))

            if n > 0 and n < len(matrix)-1:
                aux[n][contador] = matrix[n][contador]
                aux[n][m-contador] = matrix[n][m-contador]
            elif n == len(matrix)-1:
                aux[n] = matrix[n]
            n+=1

        contador += 1
        
        print(aux)
        aux = matriz_vacia(matrix)
            
    return 0    


m = 4
n = 4, 
r = 2
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16],[17,18,19,20]]
matrix = [[1, 2, 3, 4, 5, 6], [7,8,9,10,11,12], [13,14,15,16,17,18], [19,20,21,22,23,24],[25,26,27,28,29,30]]
matrix = [[1, 2, 3, 4, 5, 6, 7], [8,9,10,11,12,13,14], [15,16,17,18,19,20,21], [22,23,24,25,26,27,28],[29,30,31,32,33,34,35],[36,37,38,39,40,41,42]]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matrixRotation(matrix=matrix, r=r)