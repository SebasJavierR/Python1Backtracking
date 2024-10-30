import random
from mapa import Coord , Mapa
from pila import Pila
class IA:
    """
    Inteligencia artificial para resolver un laberinto.

    Se simula un jugador que comienza en la celda de origen, y mediante
    el método avanzar() el jugador hace un movimiento.

    Ejemplo:
        >>> mapa = Mapa(10, 10)
        >>> ia = IA()
        >>> ia.coord_jugador()
        Coord(0, 0)
        >>> while ia.coord_jugador() != mapa.destino()
        ...     ia.avanzar()
        >>> ia.coord_jugador()
        Coord(9, 9)
    """

    def __init__(self, mapa):
        """Constructor.

        Argumentos:
            mapa (Mapa): El mapa con el laberinto a resolver
        """
        self.mapa=mapa
        self.pos_jugador=mapa.origen()
        self.lista_visitados=[]
        self.pila_camino=Pila()
        self.intersecciones=[]
        self.movimientos_posibles=0

    def coord_jugador(self):
        """Coordenadas del "jugador".

        Devuelve las coordenadas de la celda en la que se encuentra el jugador.

        Devuelve:
            Coord: Coordenadas del "jugador"

        Ejemplo:
            >>> ia = IA(Mapa(10, 10))
            >>> ia.coord_jugador()
            Coord(0, 0)
            >>> ia.avanzar()
            >>> ia.coord_jugador()
            Coord(1, 0)
            >>> ia.avanzar()
            >>> ia.coord_jugador()
            Coord(2, 0)
        """
        return self.pos_jugador

    def visitados(self):
        """Celdas visitadas.

        Devuelve:
            secuencia<Coord>: Devuelve la lista (o cualqueir otra secuencia) de
            de celdas visitadas al menos una vez por el jugador desde que
            comenzó la simulación.

        Ejemplo:
            >>> ia = IA(Mapa(10, 10))
            >>> ia.avanzar()
            >>> ia.avanzar()
            >>> ia.avanzar()
            >>> ia.visitados()
            [Coord(0, 0), Coord(1, 0),  Coord(2, 0)]
        """
        return self.lista_visitados

    def camino(self):
        """Camino principal calculado.

        Devuelve:
            secuencia<Coord>: Devuelve la lista (o cualqueir otra secuencia) de
            de celdas que componen el camino desde el origen hasta la posición
            del jugador. Esta lista debe ser un subconjunto de visitados().

        Ejemplo:
            >>> ia = IA(Mapa(10, 10))
            >>> for i in range(6):
            ...     ia.avanzar()
            >>> ia.visitados()
            [Coord(0, 0), Coord(1, 0), Coord(1, 1),  Coord(2, 0),  Coord(3, 0),  Coord(4, 0)]
            >>> ia.camino()
            [Coord(0, 0), Coord(1, 0),  Coord(2, 0),  Coord(3, 0),  Coord(4, 0)]

        Nota:
            La celda actual en la que está el jugador puede no estar en la
            lista devuelta (esto tal vez permite simplificar la
            implementación).
        """
        return self.pila_camino

    def avanzar(self):
        """Avanza un paso en la simulación.

        Si el jugador no está en la celda destino, y hay algún movimiento
        posible hacia una celda no visitada, se efectúa ese movimiento.
        """
        if self.pos_jugador()==self.mapa.destino():
            return 0
        coordenada=self.pos_jugador()
        disponibles=[]
        for direccion in range(4):
            if direccion==0:
                #abajo
                avanzar=(0,1)
            if direccion==1:
                #arriba
                avanzar=(0,-1)
            if direccion==2:
                #izquierda
                avanzar=(-1,0)
            if direccion==3:
                #derecha
                avanzar=(1,0)
            if coordenada+avanzar in self.lista_visitados:
                continue
            elif self.mapa.celda_bloqueada(Coord(coordenada+avanzar)):
                continue
            else:
                self.movimientos_posibles+=1
                if not coordenada in self.intersecciones:
                    self.intersecciones.append(coordenada)
                disponibles.append(coordenada+avanzar)
        if self.movimientos_posibles==0:
            for visitados in self.lista_visitados:
                if visitados.intersecciones>0:
                    ultimo_disponible=visitados
            coord_camino=self.pila_camino.desapilar()
            while coord_camino!=ultimo_disponible:
                coord_camino=self.pila_camino.desapilar()
            self.pos_jugador=ultimo_disponible
            return self.avanzar()
        else:
            avanzar=random.randint(0,len(disponibles))
            coordenada=disponibles[avanzar]
            self.pos_jugador=coordenada
            self.lista_visitados.append(coordenada)
            self.pila_camino.apilar(coordenada)