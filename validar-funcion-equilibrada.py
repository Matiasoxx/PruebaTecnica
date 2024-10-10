#Ejercicio 3: Cree una función que permita validar que una expresión con
# paréntesis, llaves y corchetes se encuentra equilibrada (significa que
# paréntesis, llaves y corchetes de una expresión se abren y cierran en
# orden de forma correcta).


#Entrada: Se recibira una cadena de texto con los respectivos parentesis, llaves y corchetes
#Salida: Se va a indicar si la expresión se encuentra equilibrada o no
#Proceso: Se recorrera toda la cadena de texto

def validar_expresion(expresion):
    #Iremos construyendo una lista que nos permita almacenar los parentesis, llaves y corchetes
    ayudante = []
    #Determinaremos familias
    familias = {"{":"}", "[":"]", "(":")"}

    #Recorreremos toda la expresión para determinar si se encuentra equilibrada o no
    for elemento in expresion:
        #Vamos a ir alamacenando los elementos de inicializacion de parentesis, llaves y corchetes
        if elemento in familias:
            ayudante.append(elemento)
        #Vamos a almacenar los elementos de cierre de parentesis, llaves y corchetes
        elif elemento in familias.values():
            #Si la lista ayudante se encuentra vacia en este punto significa que no se abrio un parentesis, llave o corchete
            if len(ayudante) == 0:
                print(f"Expresión no equilibrada: {expresion}")
                return
            #Haremos uso de familias que es un diccionario que nos permitira determinar si se encuentra equilibrada la expresión
            # Si elemento en este momento no se encuentra en familias, significa que no se encuentra equilibrada la expresión  
            elif familias.get(ayudante[-1]) != elemento:
                print(f"Expresión no equilibrada: {expresion}")
                return
            #Si se cierra correctamente entonces eliminamos el ultimo elemento que se esta comparando
            ayudante.pop()
    #Si ya reccomimos toda la expresión y la lista ayudante se encuentra vacia, entonces la expresión se encuentra equilibrada
    if len(ayudante) == 0:
        print(f"Expresión equilibrada: {expresion}")
    #De lo contrario no se encuentra equilibrada
    else:
        print(f"Expresión no equilibrada: {expresion}")


if __name__ == "__main__":
    #Se pide al usuario que ingrese una expresión
    expresion1 = "{ [ a * ( c + d ) ] – b }"
    validar_expresion(expresion1)
    expresion2 = "{ a * ( c + d ) ] – b }"
    validar_expresion(expresion2)
