#ESTAN MARCADOS CON " ? " Los lugares que hay que completar y esta acompañado siempre por un "#" con lo que deberia ir ahi


import random
import random
from mapa import Mapa , Coord
from pila import Pila
def generar_grilla_bloqueada(filas, columnas):
    grilla = Mapa(filas,columnas)
    for x in range(filas):
        for y in range(columnas):
            coordenada=Coord(x,y) #con el visual studio te dice lo q hacen cuando pasas el mouse por arriba
            if grilla.origen() == coordenada or grilla.destino() == coordenada:
                continue
            else:
                grilla.bloquear(coordenada)
    return grilla

def direccion_valida(direccion,grilla):
    # Direccion[0] == Fila , Direccion[1] == Columna
    if (direccion[0],direccion[1]) > grilla.dimension() or (direccion[0],direccion[1]) < (0,0):
        return False
    elif grilla.celda_bloqueada(direccion[0]][direccion[1]): #bool si esta bloqueada true
        return False
    else:
        return True

def arriba(casilla_actual): 
    casilla_nueva = [casilla_actual[0]-2,casilla_actual[1]]
    casilla_intermedia = [casilla_actual[0]-1,casilla_actual[1]]
    return casilla_nueva , casilla_intermedia

def abajo(casilla_actual):
    casilla_nueva = [casilla_actual[0]+2,casilla_actual[1]]
    casilla_intermedia = [casilla_actual[0]+1,casilla_actual[1]]
    return casilla_nueva , casilla_intermedia

def izquierda(casilla_actual):
    casilla_nueva = [casilla_actual[0],casilla_actual[1]-2]
    casilla_intermedia = [casilla_actual[0],casilla_actual[1]-1]
    return casilla_nueva , casilla_intermedia

def derecha(casilla_actual):
    casilla_nueva = [casilla_actual[0],casilla_actual[1]+2]
    casilla_intermedia = [casilla_actual[0],casilla_actual[1]+1]
    return casilla_nueva , casilla_intermedia

def encerrado(casilla_actual,grilla): #return true o false

def volver(casilla_actual,grilla,lista_visitados,intersecciones,pila_camino): #cord anteriores
    ultimo_disponible="no hay"
    for visitados in lista_visitados:
        if visitados in intersecciones:
            ultimo_disponible=visitados
        coord_camino=pila_camino.desapilar()
        while coord_camino!=ultimo_disponible:
            coord_camino=pila_camino.desapilar()
        casilla_actual=ultimo_disponible
    if ultimo_disponible=="no hay"
        return False
    return casilla_actual

def se_puede_volver(?): #true o false

def generar_laberinto(filas, columnas):
    """Generar un laberinto.

    Argumentos:
        filas, columnas (int): Tamaño del mapa

    Devuelve:
        Mapa: un mapa nuevo con celdas bloqueadas formando un laberinto
              aleatorio
    """
    
    grilla = generar_grilla_bloqueada(filas,columnas)
    casilla_actual = grilla.origen() #ya esta libre porq no se bloqueo en generar
    lista_visitados = []
    intersecciones = []
    pila_camino = Pila()
    movimientos_posibles=0
    direcciones = {
        0 : [-1,-1] #Inizializacion
        1 : arriba,
        2 : abajo,
        3 : izquierda,
        4 : derecha,
    }
    while True:
        if self.pos_jugador()==self.mapa.destino():
                movimientos_posibles=0
            coordenada=casilla_actual
            disponibles=[]
            for caminos in range(4): #primero se fija todas las direcciones para guardarlas por si tiene q volver
                casilla_nueva , casilla_intermedia = direcciones[direccion](casilla_actual)
                if casilla_nueva in lista_visitados:
                    continue
                elif direccion_valida(casilla_nueva,grilla):
                    continue
                else:
                    movimientos_posibles+=1
                    if movimientos_posibles>1:
                        if not coordenada in intersecciones: #para despues
                            intersecciones.append(coordenada)
                    disponibles.append(caminos)
            if movimientos_posibles==0:
                casilla_actual=volver(casilla_actual,grilla,lista_visitados,intersecciones,pila_camino)
                if not casilla_actual: #no hay a donde volver, se termino
                    return grilla
            direccion = random.randint(1,4)
            while direccion not in disponibles:
                direccion = random.randint(1,4)
            casilla_nueva , casilla_intermedia = direcciones[direccion](casilla_actual) # [X Fila,Y Columna]
            grilla.desbloquear(casilla_nueva) #Cambiar el estado a libre 
            grilla.desbloquear(casilla_intermedia) #El estado de la casilla intermedia
            casilla_actual = casilla_nueva
    






    


    