class Pila:
    def __init__(self):
        self.tope = None

    def apilar(self, x):
        n = _Nodo(x, self.tope)
        self.tope = n

    def desapilar(self):
        if self.esta_vacia():
            raise PilaVacia()
        dato = self.tope.dato
        self.tope = self.tope.prox
        return dato

    def ver_tope(self):
        if self.esta_vacia():
            raise PilaVacia()
        return self.tope.dato

    def esta_vacia(self):
        return not self.tope

class PilaVacia(Exception):
    def __init__(self):
        super().__init__("Pila vacia")

class _Nodo:
    def __init__(self, dato, prox):
        self.dato = dato
        self.prox = prox
