import random
from mapa import Mapa , Coord

def explorar(grilla,casilla_actual):

    if grilla.es_coord_valida(casilla_actual.trasladar(-2,0)) and grilla.celda_bloqueada(casilla_actual.trasladar(-2,0)):
        grilla.desbloquear(casilla_actual.trasladar(-2,0)(casilla_actual))
        grilla.desbloquear(casilla_actual.trasladar(-1,0)(casilla_actual))
        explorar(grilla,casilla_actual.trasladar(-2,0))
    
    if grilla.es_coord_valida(casilla_actual.trasladar(2,0)) and grilla.celda_bloqueada(casilla_actual.trasladar(2,0)):
        grilla.desbloquear(casilla_actual.trasladar(2,0)(casilla_actual))
        grilla.desbloquear(casilla_actual.trasladar(1,0)(casilla_actual))
        explorar(grilla,casilla_actual.trasladar(2,0))

    if grilla.es_coord_valida(casilla_actual.trasladar(0,2)) and grilla.celda_bloqueada(casilla_actual.trasladar(0,2)):
        grilla.desbloquear(casilla_actual.trasladar(0,2)(casilla_actual))
        grilla.desbloquear(casilla_actual.trasladar(0,1)(casilla_actual))
        explorar(grilla,casilla_actual.trasladar(0,2))

    if grilla.es_coord_valida(casilla_actual.trasladar(0,-2)) and grilla.celda_bloqueada(casilla_actual.trasladar(0,-2)):
        grilla.desbloquear(casilla_actual.trasladar(0,-2)(casilla_actual))
        grilla.desbloquear(casilla_actual.trasladar(0,-1)(casilla_actual))
        explorar(grilla,casilla_actual.trasladar(0,-2))
    else:
        return grilla

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
    grilla = explorar(grilla,casilla_actual)
    return grilla



    


    