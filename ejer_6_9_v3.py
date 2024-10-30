mensaje = "¿Cuál es tu número favorito?"
min = -50
max = 50

def pedir_entero(mensaje , max, min):
    """ Esta funcion recive un numero entero maximo, un minimo y un mensaje,
    con esta informacion pide al usuario un numero entero, si se encuentra entre
    el minimo y el maximo, lo devuelve, de lo contrario devuelve un mensaje de error
    aclarando si es mayor, menor o no es un numero que cumpla los requisitos y 
    vuelve a pedir que se ingrese un numero que si cumpla.
    """
    mensaje = mensaje + " [ {}..{} ]: ".format(min,max)
    while True:
        n_original = input(mensaje)
        n_final = n_original
        if n_original[0] == "-":
            n_final = n_original
            n_original = n_original[1:]

        if n_original.isdigit(): 
            if int(n_final) > max:
                print("el valor es mayor al maximo")
            elif int(n_final) < min:
                print("el valor es inferior al minimo")
            else:
                return int(n_final)

        else:
            print("No a ingresado un numero entero")

print(pedir_entero(mensaje , max , min))
