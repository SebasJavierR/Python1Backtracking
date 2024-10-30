#ESTAN MARCADOS CON " ? " Los lugares que hay que completar y esta acompañado siempre por un "#" con lo que deberia ir ahi

import random
from mapa import Mapa , Coord
from pila import Pila


def direccion_valida(direccion,grilla):
    
    # Direccion[0] == Fila , Direccion[1] == Columna
    if not grilla.es_coord_valida(direccion):
        return False
    elif not grilla.celda_bloqueada(direccion):
        return False
    else:
        return True

def arriba(casilla_actual): 
    casilla_nueva = casilla_actual.trasladar(-2,0)
    casilla_intermedia = casilla_actual.trasladar(-1,0)
    return casilla_nueva , casilla_intermedia

def abajo(casilla_actual):
    casilla_nueva = casilla_actual.trasladar(2,0)
    casilla_intermedia = casilla_actual.trasladar(1,0)
    return casilla_nueva , casilla_intermedia

def izquierda(casilla_actual):
    casilla_nueva = casilla_actual.trasladar(0,-2)
    casilla_intermedia = casilla_actual.trasladar(0,-1)
    return casilla_nueva , casilla_intermedia

def derecha(casilla_actual):
    casilla_nueva = casilla_actual.trasladar(0,2)
    casilla_intermedia = casilla_actual.trasladar(0,1)
    return casilla_nueva , casilla_intermedia


def volver(casilla_actual,grilla,lista_visitados,intersecciones,pila_camino):
    ultimo_disponible="no hay"
    for visitados in lista_visitados:
        if visitados in intersecciones:
            ultimo_disponible=visitados
        coord_camino=pila_camino.desapilar()
        while coord_camino!=ultimo_disponible:
            coord_camino=pila_camino.desapilar()
        casilla_actual=ultimo_disponible
    if ultimo_disponible=="no hay":
        return False
    return casilla_actual

def generar_laberinto(filas, columnas):
    """Generar un laberinto.

    Argumentos:
        filas, columnas (int): Tamaño del mapa

    Devuelve:
        Mapa: un mapa nuevo con celdas bloqueadas formando un laberinto
              aleatorio
    """
    
    grilla = Mapa(filas,columnas)
    print(grilla)
    casilla_actual = grilla.origen() #ya esta libre porq no se bloqueo en generar
    lista_visitados = []
    intersecciones = []
    pila_camino = Pila()
    movimientos_posibles=0
    direcciones = {
        1 : arriba,
        2 : abajo,
        3 : izquierda,
        4 : derecha,
    }
    while True:
        if casilla_actual==grilla.destino():
            casilla_actual=volver(casilla_actual,grilla,lista_visitados,intersecciones,pila_camino)
            if not casilla_actual: #no hay a donde volver, se termino
                print(lista_visitados,movimientos_posibles)
                print(grilla.posiciones)
                return grilla
            continue
        coordenada=casilla_actual
        disponibles=[]
        for pre_direccion in range(1,5): #primero se fija todas las direcciones para guardarlas por si tiene q volver
            casilla_nueva , casilla_intermedia = direcciones[pre_direccion](casilla_actual)
            if casilla_nueva in lista_visitados:
                continue
            elif not direccion_valida(casilla_nueva,grilla):
                continue
            else:
                movimientos_posibles+=1
                if movimientos_posibles>1:
                    if not coordenada in intersecciones:
                        intersecciones.append(coordenada)
                disponibles.append(pre_direccion)
                print(disponibles)
        if movimientos_posibles==0:
            casilla_actual=volver(casilla_actual,grilla,lista_visitados,intersecciones,pila_camino)
            if not casilla_actual: #no hay a donde volver, se termino
                print(lista_visitados,movimientos_posibles)
                print(grilla.posiciones)
                return grilla
            continue
        direccion = random.randint(1,5)
        while direccion not in disponibles:
            direccion = random.randint(1,5)
        casilla_nueva , casilla_intermedia = direcciones[direccion](casilla_actual) # [X Fila,Y Columna]
        grilla.desbloquear(casilla_nueva) #Cambiar el estado a libre 
        grilla.desbloquear(casilla_intermedia) #El estado de la casilla intermedia
        casilla_actual = casilla_nueva
        movimientos_posibles=0



    


    