matriz = [['☐','☐','☐','☐','☐'],['☐','☐','☐','☐','☐'],['☐','☐','☐','☐','☐'],['☐','☐','☐','☐','☐'],['☐','☐','☐','☐','☐']]

import os
correcto = '✔'
incorrecto = '✘'

ls_preguntas = ['¿Qué es Python?\n\n1. Juego\n2. Lenguaje de programación\n3. Marca de auto\n4. Ninguna de las anteriores',
                '¿Qué es HTML?\n\n1. Lenguaje de maquetación\n2. Marca de gaseosa\n3. Navegador\n4. Perro caliente', 'Apple es una marca de...\n\n1. Carros\n2. ']
ls_respuesta = ['2', '1']

def fnt_pintarMatriz():
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end='   ')
        print('\n\n')
        

contador = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        os.system('cls')
        fnt_pintarMatriz()
        print()
        print(ls_preguntas[contador])
        print()
        r = input('->')
        if r == ls_respuesta[contador]:
            matriz[i][j] = correcto
        else:
            matriz[i][j] = incorrecto
            contador += 1