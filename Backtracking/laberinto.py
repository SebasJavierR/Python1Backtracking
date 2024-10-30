#ESTAN MARCADOS CON " ? " Los lugares que hay que completar y esta acompañado siempre por un "#" con lo que deberia ir ahi


import random

def generar_grilla_bloqueada(filas, columnas):
    grilla = []
    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            fila.append(?)#Estado vacio
        grilla.append(fila)
    return grilla

def direccion_es_valida(direccion,grilla):
    # Direccion[0] == Fila , Direccion[1] == Columna
    if not direccion[0] > len(grilla) and not direccion[0] < 0 and not direccion[1] > len(grilla[0]) and not direccion[1] < 0:
        return False
    elif grilla[direccion[0]][direccion[1]] != ?: #Estado vacio
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

def volver(casilla_actual,grilla): #cord anteriores

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
    casilla_actual = [1,1] #[X Fila,Y Columna]
    direcciones = {
        0 : [-1,-1] #Inizializacion
        1 : arriba,
        2 : abajo,
        3 : izquierda,
        4 : derecha,
    }


    grilla[casilla_actual[0]][casilla_actual[1]] = ? #Estado "Libre"
    while not se_puede_volver() and not encerrado(casilla_actual) # Usar el Backtracking
        while not encerrado(casilla_actual,grilla):
            direccion = 0
            while direccion_es_valida(direcciones[direccion](),grilla) != False:
                direccion = random.randint(1,4)
            casilla_nueva , casilla_intermedia = direcciones[direccion](casilla_actual) # [X Fila,Y Columna]
            grilla[nueva_casilla[0]][nueva_casilla[1]] = ? #Cambiar el estado a libre 
            grilla[casilla_intermedia[0]][casilla_intermedia[1]] #El estado de la casilla intermedia
            casilla_actual = casilla_nueva

        casilla_actual = volver(casilla_actual,grilla)






    


    