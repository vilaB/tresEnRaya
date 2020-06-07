


def imprimir_tablero(tablero, extremos=False):
    fila=0
    columna=0
    for linea in tablero:
        #Linea de huecos 1
        if fila != 0:
            for elemento in linea:
                print("-----", end="")
                if columna != len(linea) - 1:
                    print("|", end="")
                columna += 1
        elif extremos:
            for elemento in linea:
                print("     ", end="")
                if columna != len(linea) - 1:
                    print("|", end="")
                columna += 1
        columna=0
        print("")

        #Impresión de la línea con números 2
        for elemento in linea:
            if isinstance(elemento, str) or  elemento<10:
                print("  " + str(elemento) + "  ", end="")
            else:
                print(" " + str(elemento) + "  ", end="")
            if columna != len(linea) - 1:
                print("|", end="")
            columna+=1
        columna=0
        print("")

        #Final de línea 3
        if fila == len(tablero)-1 and extremos:
            for elemento in linea:
                print("     ", end="")
                if columna != len(linea) - 1:
                    print("|", end="")
                columna += 1

        fila +=1
        columna=0
    print("")

def crear_tablero(alto=3, ancho=3):

    tablero = []
    numeroCasilla=1
    for i in range(alto):
        tablero.append([])
        for j in range(ancho):
            tablero[len(tablero)-1].append(numeroCasilla)
            numeroCasilla+=1
    return tablero

def elegir_nombres():
    while True:
        jugador_1 = input("Nombre del jugador 1:\n>")
        jugador_2 = input("Nombre del jugador 2:\n>")
        if jugador_1 != jugador_2:
            break
        else:
            print("Los nombres deben de ser distintos")

    return jugador_1,jugador_2

import math
def colocar_ficha(tablero, jugador):
    while True:
        imprimir_tablero(tablero, extremos=True)
        print("Es turno de " + jugador)
        casilla = int(input( "¿Dónde quieres colocar la ficha?\n>"))
        if casilla > len(tablero) * len(tablero[0]) or casilla <= 0:
            print("Ese valor no está en el tablero.")
            continue
        casilla -=1
        fila = math.floor(casilla/len(tablero[0]))
        if tablero[fila][casilla - (fila * len(tablero[0]))] != casilla + 1:
            print("Esta casilla ya está cogida, elige otra!")
            continue
        tablero[fila][casilla - (fila * len(tablero[0]))] = jugador[0]

        #Comprobar si ganamos
        final = hay_ganador(tablero)
        if final != None:
            imprimir_tablero(tablero, extremos=True)
            print("Tenemos ganador!" + " El jugador " + jugador + " ha ganado!")
            return True
        return False

#Podria pasarse la casilla y comprobar solo si esta provoca que alguien gane
#Más eficiente
def hay_ganador(tablero):
    #filas
    for linea in tablero:
        iguales = True                                          #Asumimos que todos en la linea son iguales
        for i in range(1,3):
            if linea[i-1] != linea[i]:                          #Comprobamos entre pares
                iguales = False
                break                                           #Si alguno es distinto deja de mirar la linea
        if iguales:
            return linea[0]                               #Devuelve el ganador, pues es cualquiera de esta linea
    #Columnas
    #Basicamente hacemos la traspuesta y la misma operación que antes
    tableroAux = []
    for i in range(len(tablero[0])):
        tableroAux.append([])
        for j in range(len(tablero)):
            tableroAux[len(tableroAux)-1].append(tablero[j][i])
    for linea in tableroAux:
        iguales = True                                          #Asumimos que todos en la linea son iguales
        for i in range(1,3):
            if linea[i-1] != linea[i]:                          #Comprobamos entre pares
                iguales = False
                break                                           #Si alguno es distinto deja de mirar la linea
        if iguales:
            return linea[0]
    #Diagonales
    tableroAux = []
    tableroAux.append([])
    tableroAux[0].append(tablero[0][0])
    tableroAux[0].append(tablero[1][1])
    tableroAux[0].append(tablero[2][2])

    tableroAux.append([])
    tableroAux[1].append(tablero[0][2])
    tableroAux[1].append(tablero[1][1])
    tableroAux[1].append(tablero[2][0])
    for linea in tableroAux:
        iguales = True                                          #Asumimos que todos en la linea son iguales
        for i in range(1,3):
            if linea[i-1] != linea[i]:                          #Comprobamos entre pares
                iguales = False
                break                                           #Si alguno es distinto deja de mirar la linea
        if iguales:
            return linea[0]

    return None

def juego():
    #Iniciando el juego
    #while True:
    #    alto = int(input("Indica el alto\n>"))
    #    ancho = int(input("Indica el ancho\n>"))
    #    if alto > 0 and ancho > 0:
    #        break
    tablero = crear_tablero()
    imprimir_tablero(tablero, extremos=True)
    j1,j2 = elegir_nombres()
    print("Así que " + j1 + " y " + j2 +". Vamos a ver que sabéis hacer!")

    #Jugado
    jugadores = [j1,j2]
    jugador_actual = j1
    en_juego=True
    while en_juego:
        final = colocar_ficha(tablero, jugador_actual)

        if final:
            break
        if jugador_actual == j1:
            jugador_actual = j2
        else:
            jugador_actual=j1



juego()
