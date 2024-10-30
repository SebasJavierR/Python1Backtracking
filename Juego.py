import terminal
import random

tablero = [8,8] #[Filas,Columnas]
velocidad = 1
victoria = 5

def esta_en_serp(serpiente,i,j):
    """recive la serpiente y dos cordenadas y juzga si son iguales a alguna
    de las ubicaciones en las que esta la serpiente
    """
    for v in range(len(serpiente)):
        if serpiente[v][0] == i and serpiente[v][-1] == j:
            return True
    return False

def display(tablero, mostrar):
    """Esta funcion recive las medidas del tablero y una matriz para imprimirla linea por linea
    """ 
    for j in range(tablero[0]):
        linea = "."
        for i in range(tablero[-1]):
            linea = linea + str(mostrar[j][i] +".")
        print(linea)
    return

def convinar(tablero,fruta,serpiente):
    """ Esta funcion convina la fruta la serpiente en un matriz de las dimenciones
    indicadas por tablero, devuelve la matriz resultante
    """
    matriz = []
    for i in range(tablero[0]): #filas
        fila = []
        for j in range(tablero[-1]): #columnas  
            if esta_en_serp(serpiente,i,j):
                fila.append("#")
            elif fruta[0] == i and fruta[-1] == j:
                fila.append("*")
            else:
                fila.append(" ")
        matriz.append(fila)
    return matriz

def nueva_pos(direccion,serpiente): #[Fila,columna] lista
    if direccion == "a":
        nuevo_punto = [serpiente[-1][0] , serpiente[-1][-1] -1]
    if direccion == "d":
        nuevo_punto = [serpiente[-1][0] , serpiente[-1][-1] +1]
    if direccion == "s":
        nuevo_punto = [serpiente[-1][0] +1 , serpiente[-1][-1]]
    if direccion == "w":
        nuevo_punto = [serpiente[-1][0] -1 , serpiente[-1][-1]]
    return nuevo_punto

def pantalla(serpiente,fruta, tablero, victoria):
    """Esta funcion recive la serpiente, la fruta y el tablero,
    con estos parametros genera un tablero del juego
    """
    terminal.clear_terminal()
    mostrar = convinar(tablero,fruta,serpiente)
    print("")
    display(tablero, mostrar)
    print("")
    print("Muevete con A/S/D/W")
    print("la victoria se logra con "+ str(victoria) + " puntos")
    print("la fruta esta en: ", fruta)
    return

def generar_fruta(serpiente,tablero):
    """Esta funcion resive la serpiente y el tablero y genera un objetivo
    dentro del tablero y que no coinsida con la serpiente
    """
    while True:
        objetivo = [random.randint(0,tablero[0]-1),random.randint(0,tablero[-1]-1)] # [Fila,Columna]
        for h in range(len(serpiente)):
            if objetivo[0] == serpiente[h][0] and objetivo[-1] == serpiente[h][-1]: #evitar que el objetivo se genere sobre la serpiente
                break
            if h == len(serpiente)-1 and (objetivo[0] != serpiente[h][0] or objetivo[-1] != serpiente[h][-1]):
                return objetivo
    return objetivo

def choco_pared(nuevo_punto,serpiente,tablero):
    """ Esta funcion recive el nuevo punto, la serpiente y la tabla y comprueba si choco
    contra la pared o no, devuelve verdadero o falso si la situacion se dio o no
    """
    if nuevo_punto[0] > tablero[0]-1 or nuevo_punto[-1] > tablero[-1]-1:
        return True
    if nuevo_punto[0] < 0 or nuevo_punto[-1] < 0:
        return True
    return False

def choco_ella_misma(nuevo_punto,serpiente):
    """Esta funcion resive el nuevo punto y la serpiente y comprueba si choco con si misma,
    devuelve verdadero o falso si la situacion se dio o no
    """
    
    for h in range(len(serpiente)-1):
        if nuevo_punto[0] == serpiente[h][0] and nuevo_punto[-1] == serpiente[h][-1]:
            return True
    return False

def choco(nuevo_punto,serpiente,tablero):
    """Esta funcion recive el nuevo punto, la serpiente y el tablero
    y hace de menu para las funciones que comprueban si choco con la pared
    la serpiente o con si misma, para devolver verdadero o falso si dan estas
    situaciones
    """
    if choco_pared(nuevo_punto,serpiente,tablero):
        print("La serpiente choco con la pared!")
        return True
    if choco_ella_misma(nuevo_punto,serpiente):
        print("La serpiente choco consigo misma!")
        return True
    return False

def menu(tablero,velocidad):
    """Esta funcion recive un tablero y la velocidad, con ello 
    funciona como "menu" para el funcionamiento del juego.
    """
    crece = 0
    serpiente = [[tablero[0]//2 , tablero[-1]//2]]
    ultima_direccion = "w"
    fruta = generar_fruta(serpiente,tablero)
    puntuacion = 0
    while True:

        pantalla(serpiente,fruta,tablero,victoria)

        nueva_direccion = terminal.timed_input(velocidad)
        try:
            if nueva_direccion[0] == "w" or nueva_direccion[0] == "a" or nueva_direccion[0] == "s" or nueva_direccion[0] == "d":
                direccion = nueva_direccion[0]
                ultima_direccion = nueva_direccion[0]
            else:
                direccion = ultima_direccion
        except:
            direccion = ultima_direccion
        
        nuevo_punto = nueva_pos(direccion,serpiente)

        if nuevo_punto == fruta:
            fruta = generar_fruta(serpiente,tablero)
            puntuacion = puntuacion + 1
            crece = 1

        if choco(nuevo_punto,serpiente,tablero):
            print("Perdiste...")
            print("tu puntuacion fue de", puntuacion)
            break

        if crece == 0:
            serpiente.append(nuevo_punto)
            serpiente.pop(0)
        if crece == 1:
            serpiente.append(nuevo_punto)
            crece = 0     
        if puntuacion == victoria:
            print("Felicidades Usted a llegado al objetivo de " + str(victoria) + " puntos, ganaste!")
            break
    return

menu(tablero,velocidad)
