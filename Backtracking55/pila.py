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
    
    def __iter__(self):
        pila_aux=Pila()
        lista=[]
        while not self.esta_vacia():
            bloque=self.desapilar()
            lista.append(bloque)
            pila_aux.apilar(bloque)
        while not pila_aux.esta_vacia():
            self.apilar(pila_aux.desapilar())
        return iter(lista)

class PilaVacia(Exception):
    def __init__(self):
        super().__init__("Pila vacia")

class _Nodo:
    def __init__(self, dato, prox):
        self.dato = dato
        self.prox = prox
