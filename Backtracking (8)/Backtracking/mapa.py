BLOQUEADA = 0
VISITADA = 1
NO_VISITADA = 2

class Coord:
    """
    Representa las coordenadas de una celda en una grilla 2D, representada
    como filas y columnas. Las coordendas ``fila = 0, columna = 0`` corresponden
    a la celda de arriba a la izquierda.

    Las instancias de Coord son inmutables.
    """

    def __init__(self, fila=0, columna=0):
        """Constructor.

        Argumentos:
            fila, columna (int): Coordenadas de la celda
        """
        
        self.fila=fila
        self.columna=columna

    def trasladar(self, df, dc):
        """Trasladar una celda.

        Devuelve una nueva instancia de Coord, correspondiente a las coordenadas
        de la celda que se encuentra ``df`` filas y ``dc`` columnas de distancia.

        Argumentos:
            df (int): Cantidad de filas a trasladar
            dc (int): Cantidad de columnas a trasladar

        Devuelve:
            Coord: Las coordenadas de la celda trasladada
        """
        fila=self.fila+df
        columna=self.columna+dc
        return Coord(fila,columna)

    def distancia(self, otra):
        """Distancia entre dos celdas.

        Argumentos:
            otra (Coord)

        Devuelve:
            int|float: La distancia entre las dos celdas (no negativo)
        """
        return ((self.fila-otra.fila)**2+(self.columna-otra.columna)**2)**0.5

    def __eq__(self, otra):
        """Determina si dos coordenadas son iguales"""
        if self.fila==otra.fila and self.columna==otra.columna:
            return True
        else:
            return False

    def __iter__(self):
        """Iterar las componentes de la coordenada.
        Devuelve un iterador de forma tal que:
        >>> coord = Coord(3, 5)
        >>> f, c = coord
        >>> assert f == 3
        >>> assert c == 5
        """
        coorednadas=(self.fila,self.columna)
        iterador = iter(coorednadas)
        return iterador

    def __hash__(self):
        """Código "hash" de la instancia inmutable."""
        # Este método es llamado por la función de Python hash(objeto), y debe devolver
        # un número entero.
        # Más información (y un ejemplo de cómo implementar la funcion) en:
        # https://docs.python.org/3/reference/datamodel.html#object.__hash__
        return hash((self.fila,self.columna))

    def __repr__(self):
        """Representación de la coordenada como cadena de texto"""
        return repr((self.fila, self.columna))

    def __str__(self):
        return f"Fila: {self.fila} Columna: {self.columna}"

class Mapa:
    """
    Representa el mapa de un laberinto en una grilla 2D con:

    * un tamaño determinado (filas y columnas)
    * una celda origen
    * una celda destino
    * 0 o más celdas "bloqueadas", que representan las paredes del laberinto

    Las instancias de Mapa son mutables.
    """
    def __init__(self, filas, columnas):
        """Constructor.

        El mapa creado tiene todas las celdas desbloqueadas, el origen en la celda
        de arriba a la izquierda y el destino en el extremo opuesto.

        Argumentos:
            filas, columnas (int): Tamaño del mapa
        """
        #self.BLOQUEADA = 0
        #self.VISITADA = 1
        #self.NO_VISITADA = 2
        self.filas=filas
        self.columnas=columnas
        self.coord_origen=Coord(1,1)
        self.coord_destino=Coord(filas-2,columnas-2)
        self.posiciones = {}
        for x in range(columnas):
            for y in range(filas):
                self.posiciones[Coord(y,x)]= BLOQUEADA
        self.posiciones[self.coord_origen]=VISITADA
        self.posiciones[self.coord_destino]=NO_VISITADA

    def __str__(self):
        return f"{self.filas}x{self.columnas}, origen: {self.coord_origen}, destino: {self.coord_destino}"

    def dimension(self):
        """Dimensiones del mapa (filas y columnas).

        Devuelve:
            (int, int): Cantidad de filas y columnas
        """
        return (int(self.filas),int(self.columnas))

    def origen(self):
        """Celda origen.

        Devuelve:
            Coord: Las coordenadas de la celda origen
        """
        return self.coord_origen

    def destino(self):
        """Celda destino.

        Devuelve:
            Coord: Las coordenadas de la celda destino
        """
        return self.coord_destino

    def asignar_origen(self, coord):
        """Asignar la celda origen.

        Argumentos:
            coord (Coord): Coordenadas de la celda origen
        """
        self.coord_origen=coord


    def asignar_destino(self, coord):
        """Asignar la celda destino.

        Argumentos:
            coord (Coord): Coordenadas de la celda destino
        """
        self.coord_destino=coord

    def celda_bloqueada(self, coord):
        """¿La celda está bloqueada?

        Argumentos:
            coord (Coord): Coordenadas de la celda

        Devuelve:
            bool: True si la celda está bloqueada
        """
        if not self.es_coord_valida(coord):
            raise ImportError
        elif self.posiciones[coord] == BLOQUEADA:
            return True
        else: 
            return False

    def bloquear(self, coord):
        """Bloquear una celda.

        Si la celda estaba previamente bloqueada, no hace nada.

        Argumentos:
            coord (Coord): Coordenadas de la celda a bloquear
        """
        if not self.celda_bloqueada(coord):
            self.posiciones[coord]=BLOQUEADA

    def desbloquear(self, coord):
        """Desbloquear una celda.

        Si la celda estaba previamente desbloqueada, no hace nada.

        Argumentos:
            coord (Coord): Coordenadas de la celda a desbloquear
        """
        
        if self.celda_bloqueada(coord):
            self.posiciones[coord]= NO_VISITADA
    def visitadar(self, coord):
        """Visita una celda.

        Si la celda estaba previamente desbloqueada o bloqueada la cambia a visitada.

        Argumentos:
            coord (Coord): Coordenadas de la celda a desbloquear
        """
        
        if self.celda_bloqueada(coord):
            self.posiciones[coord]= VISITADA

    def alternar_bloque(self, coord):
        """Alternar entre celda bloqueada y desbloqueada.

        Si la celda estaba previamente desbloqueada, la bloquea, y viceversa.

        Argumentos:
            coord (Coord): Coordenadas de la celda a alternar
        """
        if self.celda_bloqueada(coord):
            return self.desbloquear(coord)
        else:
            return self.bloquear(coord)

    def es_coord_valida(self, coord):
        """¿Las coordenadas están dentro del mapa?

        Argumentos:
            coord (Coord): Coordenadas de una celda

        Devuelve:
            bool: True si las coordenadas corresponden a una celda dentro del mapa
        """
        if coord.fila < 0:
            return False
        if coord.columna < 0:
            return False
        if coord.columna > self.columnas-1:
            return False
        if coord.fila > self.filas-1:
            return False
        return True

    def trasladar_coord(self, coord, df, dc):
        """Trasladar una coordenada, si es posible.

        Argumentos:
            coord: La coordenada de una celda en el mapa
            df, dc: La traslación a realizar

        Devuelve:
            Coord: La coordenada trasladada si queda dentro del mapa. En caso
                   contrario, devuelve la coordenada recibida.
        """
        if not self.es_coord_valida(coord.trasladar(df,dc)):
            return coord
        else:
            return coord.trasladar(df,dc)


    def __iter__(self):
        """Iterar por las coordenadas de todas las celdas del mapa.

        Se debe garantizar que la iteración cubre todas las celdas del mapa, en
        cualquier orden.

        Ejemplo:
            >>> mapa = Mapa(10, 10)
            >>> for coord in mapa:
            >>>     print(coord, mapa.celda_bloqueada(coord))
        """
        mapa=self.dimension()
        lista_mapa=[]
        for y in range(mapa[0]):
            for x in range(mapa[1]):
                lista_mapa.append(Coord(y,x))
        iterador=iter(lista_mapa)
        return iterador