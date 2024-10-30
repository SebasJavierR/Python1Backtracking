import random
from mapa import Mapa , Coord

def arriba(casilla_actual,grilla): 
    if grilla.es_coord_valida(casilla_actual.trasladar(-2,0)) and grilla.celda_bloqueada(casilla_actual.trasladar(-2,0)):
        grilla.desbloquear(casilla_actual.trasladar(-2,0))
        grilla.desbloquear(casilla_actual.trasladar(-1,0))
        explorar(grilla,casilla_actual.trasladar(-2,0))
    return

def abajo(casilla_actual,grilla):
    if grilla.es_coord_valida(casilla_actual.trasladar(2,0)) and grilla.celda_bloqueada(casilla_actual.trasladar(2,0)):
        grilla.desbloquear(casilla_actual.trasladar(2,0))
        grilla.desbloquear(casilla_actual.trasladar(1,0))
        explorar(grilla,casilla_actual.trasladar(2,0))
    return

def izquierda(casilla_actual,grilla):
    if grilla.es_coord_valida(casilla_actual.trasladar(0,2)) and grilla.celda_bloqueada(casilla_actual.trasladar(0,2)):
        grilla.desbloquear(casilla_actual.trasladar(0,2))
        grilla.desbloquear(casilla_actual.trasladar(0,1))
        explorar(grilla,casilla_actual.trasladar(0,2))
    return

def derecha(casilla_actual,grilla):
    if grilla.es_coord_valida(casilla_actual.trasladar(0,-2)) and grilla.celda_bloqueada(casilla_actual.trasladar(0,-2)):
        grilla.desbloquear(casilla_actual.trasladar(0,-2))
        grilla.desbloquear(casilla_actual.trasladar(0,-1))
        explorar(grilla,casilla_actual.trasladar(0,-2))
    return

def explorar(grilla,casilla_actual):
    azar = random.randint(1,4)
    if azar == 1:   
        derecha(casilla_actual,grilla)
        izquierda(casilla_actual,grilla)
        abajo(casilla_actual,grilla)
        arriba(casilla_actual,grilla)
        return grilla,casilla_actual
    elif azar == 2:
        arriba(casilla_actual,grilla)
        izquierda(casilla_actual,grilla)
        derecha(casilla_actual,grilla)
        abajo(casilla_actual,grilla)
        return grilla,casilla_actual
    elif azar == 3:
        izquierda(casilla_actual,grilla)
        abajo(casilla_actual,grilla)
        derecha(casilla_actual,grilla)
        arriba(casilla_actual,grilla)
        return grilla,casilla_actual
    else:
        abajo(casilla_actual,grilla)
        derecha(casilla_actual,grilla)
        arriba(casilla_actual,grilla)
        izquierda(casilla_actual,grilla)
        return grilla,casilla_actual

def generar_laberinto(filas, columnas):
    """Generar un laberinto.

    Argumentos:
        filas, columnas (int): Tamaño del mapa

    Devuelve:
        Mapa: un mapa nuevo con celdas bloqueadas formando un laberinto
              aleatorio
    """
    
    grilla = Mapa(filas,columnas)
    casilla_actual = grilla.origen()
    grilla,casilla_actual = explorar(grilla,casilla_actual)
    n=random.randint(0,1)
    if n==1:
        grilla.desbloquear(grilla.destino().trasladar(0,-1))
    else:
        grilla.desbloquear(grilla.destino().trasladar(-1,0))

    return grilla



    


    