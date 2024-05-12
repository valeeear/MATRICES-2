matriz = [['☐','☐','☐','☐','☐'],['☐','☐','☐','☐','☐'],['☐','☐','☐','☐','☐'],['☐','☐','☐','☐','☐'],['☐','☐','☐','☐','☐']]

import os
correcto = '✔'
incorrecto = '✘'

ls_preguntas = ['¿Qué es Python?\n\n1. Juego\n2. Lenguaje de programación\n3. Marca de auto\n4. Ninguna de las anteriores',
                '¿Qué es HTML?\n\n1. Lenguaje de maquetación\n2. Marca de gaseosa\n3. Navegador\n4. Perro caliente', 'Apple es una marca de...\n\n1. Carros\n2. Alimentos\n3. Combustibles\n4. Dispositvos tecnologicos', '¿Qué es phishing?\n\n1. Un tipo de pesca deportiva\n2. Un método para obtener información personal de forma fraudulenta, generalmente a través de correos electrónicos o sitios web falsos\n3. Un metodo para mejorar la velocidad del internet','¿Qué es un algoritmo\n\n1. Una serie de instrucciones precisas para resolver un problema o realizar una tarea\n2. Un tipo de virus informático\n3. Un dispositivo de hardware para almacenamiento de datos', '¿Cuál de estos no es un tipo de archivo de imagen común?\n\n1. JPG\n2. HTML\n3. PNG', '¿Cuál de estos no es un sistema operativo?\n\n1. Windows\n2. iOS\n3. Excel','¿Qué es un firewall?\n\n1. Una pared física de protección para computadoras\n2. Un software de seguridad que controla el tráfico de red\n3. Un programa antivirus', '¿Qué es un navegador web?\n\n1. Un programa para editar imágenes\n2. Una aplicación para enviar correos electrónicos\n3. Un software para acceder y ver páginas en internet', '¿Qué es un código QR?\n\n1. Un tipo de código de barras bidimensional que puede almacenar información como direcciones web o información de contacto\n2. Un tipo de virus informático\n3. Un tipo de código postal', '¿Qué es el streaming?\n\n1. Un método para descargar archivos de internet\n2. La transmisión de contenido multimedia a través de internet en tiempo real\n3. Un tipo de protocolo de seguridad en internet']



ls_respuesta = ['2', '3', '4', '2', '1','2', '3', '2','3','1','2']

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