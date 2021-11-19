from sudoku import *
import mapas
import random

def _obtener_sudoku_enunciado():
    '''
    Devuelve un juego de sudoku creado con la representación que está en la
    documentación de sudoku.crear_juego. 
    
    Para simplificar, en las pruebas se referirá a este sudoku como
    SUDOKU_ENUNCIADO.
    '''

    return [
        [0, 0, 3,  0, 2, 0,  6, 0, 0],
        [9, 0, 0,  3, 0, 5,  0, 0, 1],
        [0, 0, 1,  8, 0, 6,  4, 0, 0],
        [0, 0, 8,  1, 0, 2,  9, 0, 0],
        [7, 0, 0,  0, 0, 0,  0, 0, 8],
        [0, 0, 6,  7, 0, 8,  2, 0, 0],
        [0, 0, 2,  6, 0, 9,  5, 0, 0],
        [8, 0, 0,  2, 0, 3,  0, 0, 9],
        [0, 0, 5,  0, 1, 0,  3, 0, 0],
    ]


def pedir_accion(sudoku):
    if not hay_movimientos_posibles(sudoku):
        if esta_terminado(sudoku):
            print("felicidades, has logrado terminar el sudoku")
            return 0
        else:
            print("Debes borrar un valor para poder continuar")
            return 2
    accion = input("ingrese una accion para continuar, para insertar un valor presione 1, para borrar un valor presione 2, 3 para salir ")
    while not accion.isdigit():
        accion = input("ingrese una accion para continuar, para insertar un valor presione 1, para borrar un valor presione 2, 3 para salir ")
    accion = int(accion)
    if accion == 1:
        return 1
    elif accion == 2:
        return 2     
    return 3
      
def pedir_jugada(accion):
    if accion == 1:
        jugada = input("Ingrese los valores que desea insertar seguidos de una coma [f,c,v]: ")
        return jugada
    elif accion == 2:
        jugada = input("Ingrese el valor de la fila y columna de la posicion que desea eliminar seguidos de una coma [f,c]: ")
        return jugada
    jugada = 'salir'
    return jugada


def cambiar_letra_por_numero(letra):
    if letra in 'abcdefghi':
        return 'abcdefghi'.index(letra)
    return 0


def imprimir_juego(sudoku):
    letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    print('    1 2 3   4 5 6   7 8 9')
    print('   ----------------------- ')
    
    for i in range(9):
        print(letras[i], end= ' ')
        print('|', end=' ')
        for j in range(9):
            if j % 3 == 2:
                if sudoku[i][j] == 0:
                    print(' ', end = ' | ')      
                else:                          
                    print(str(sudoku[i][j]), end = ' | ')
            elif sudoku[i][j] == 0:
                print(' ', end = ' ')
            else:
                print(str(sudoku[i][j]), end = ' ')
        if i % 3 != 2:
            print(letras[i])
        elif i != 8:   
            print(letras[i])
            print('    - - -   - - -   - - -')

    print(letras[i])        
    print('   ----------------------- ')    
    print('    1 2 3   4 5 6   7 8 9')



def sudoku_random():
    representacion = mapas.MAPAS[random.randint(0, 49)]
    sudoku = crear_juego(representacion)
    return sudoku

def jugar_juego():
    sudoku = sudoku_random()
    imprimir_juego(sudoku)
    accion = pedir_accion(sudoku)
    jugada = pedir_jugada(accion)
    while(jugada != 'salir'):
        if accion == 1:
            lista_valores = jugada.split(',')
            fila, columna, valor = cambiar_letra_por_numero(lista_valores[0]), int(lista_valores[1]) - 1, int(lista_valores[2])
            if not es_movimiento_valido(sudoku, fila, columna, valor):
                print("El movimiento no es valido")
            else:
                sudoku = insertar_valor(sudoku, fila, columna, valor)

        else:
            lista_valores = jugada.split(',')
            fila, columna = cambiar_letra_por_numero(lista_valores[0]), int(lista_valores[1]) - 1
            sudoku = borrar_valor(sudoku, fila, columna)
        
        imprimir_juego(sudoku)
        accion = pedir_accion(sudoku)
        jugada = pedir_jugada(accion)


