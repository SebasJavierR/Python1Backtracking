#def generar_grilla_bloqueada(filas, columnas):
#    grilla = []
#    for _ in range(filas):
#        fila = []
#        for _ in range(columnas):
#            fila.append("Pared")
#        grilla.append(fila)
#
#    return grilla
#
#grilla = generar_grilla_bloqueada(5,10)
#for h in range(5):
#    print(grilla[h])


def arriba():
    return 1
def abajo():
    return 2
def izquierda():
    return 3
def derecha ():
    return 4
import random
direcciones = {
    1 : arriba,
    2 : abajo,
    3 : izquierda,
    4 : derecha,
}
print(direcciones[random.randint(1,4)]())
