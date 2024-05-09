matriz = [['☐','☐','☐','☐','☐'],['☐','☐','☐','☐','☐'],['☐','☐','☐','☐','☐'],['☐','☐','☐','☐','☐'],['☐','☐','☐','☐','☐']]

correcto = '✔'
incorrecto = '✘'

ls_preguntas = ['¿Qué es Python?', '¿Qué es HTML?']
ls_respuesta = ['2', '1']


def fnt_agregar(x,y):
    if x == 0 and y == 0:
        if matriz[x][y] == '☐':
            matriz[x][y] = correcto.upper()
    elif x == 0 and y == 1:
        if matriz[x][y] == '☐':
            matriz[x][y] = correcto.upper()
    elif x == 0 and y == 2:
        if matriz[x][y] == '☐':
            matriz[x][y] = incorrecto.upper()
    elif x == 0 and y == 3:
        if matriz[x][y] == '☐':
            matriz[x][y] = incorrecto.upper()
    elif x == 0 and y == 4:
        if matriz[x][y] == '☐':
            matriz[x][y] = incorrecto.upper()
    elif x == 1 and y == 0:
        if matriz[x][y] == '☐':
            matriz[x][y] = correcto.upper()
    elif x == 1 and y == 1:
        if matriz[x][y] == '☐':
            matriz[x][y] = incorrecto.upper()
    elif x == 1 and y == 2:
        if matriz[x][y] == '☐':
            matriz[x][y] = incorrecto.upper()
    elif x == 1 and y == 3:
        if matriz[x][y] == '☐':
            matriz[x][y] = correcto.upper()
    elif x == 1 and y == 4:
        if matriz[x][y] == '☐':
            matriz[x][y] = correcto.upper()
    elif x == 2 and y == 0:
        if matriz[x][y] == '☐':
            matriz[x][y] = correcto.upper()
    elif x == 2 and y == 1:
        if matriz[x][y] == '☐':
            matriz[x][y] = incorrecto.upper()
    elif x == 2 and y == 2:
        if matriz[x][y] == '☐':
            matriz[x][y] = incorrecto.upper()
    elif x == 2 and y == 3:
        if matriz[x][y] == '☐':
            matriz[x][y] = correcto.upper()
    elif x == 2 and y == 4:
        if matriz[x][y] == '☐':
            matriz[x][y] = incorrecto.upper()
    elif x == 3 and y == 0:
        if matriz[x][y] == '☐':
            matriz[x][y] = correcto.upper()
    elif x == 3 and y == 1:
        if matriz[x][y] == '☐':
            matriz[x][y] = incorrecto.upper()
    elif x == 3 and y == 2:
        if matriz[x][y] == '☐':
            matriz[x][y] = correcto.upper()
    elif x == 3 and y == 3:
        if matriz[x][y] == '☐':
            matriz[x][y] = correcto.upper()
    elif x == 3 and y == 4:
        if matriz[x][y] == '☐':
            matriz[x][y] = incorrecto.upper()
    elif x == 4 and y == 0:
        if matriz[x][y] == '☐':
            matriz[x][y] = correcto.upper()
    elif x == 4 and y == 1:
        if matriz[x][y] == '☐':
            matriz[x][y] = correcto.upper()
    elif x == 4 and y == 2:
        if matriz[x][y] == '☐':
            matriz[x][y] = correcto.upper()
    elif x == 4 and y == 3:
        if matriz[x][y] == '☐':
            matriz[x][y] = incorrecto.upper()
    elif x == 4 and y == 4:
        if matriz[x][y] == '☐´                                                                                                                                                                                                                                                                                                                                                                                     ':
            matriz[x][y] = correcto.upper()
    
    
                    
def fnt_impresion_matriz():
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=' ')
        print()

sw = True
while sw == True:
    import os
    os.system('cls')
    fnt_impresion_matriz()
    fnt_agregar(int(input('Fila:  ')),int(input('Columna:  ')))