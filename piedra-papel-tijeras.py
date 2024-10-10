
#Ejercicio 4: Piedra(R), papel(P) o tijera(S)
#Se requiere crear una función que permita determinar quien es el ganador de un mejor de 5 (Un jugador requiere de 3 victorias para ganar) para el juego de “Piedra, Papel o Tijera”.


#Funcion para leer la jugada de los jugadores del objeto JSON
# Entrada: Recibe un objeto JSON con las jugadas de los jugadores
# Salida: Retorna el resultado de las rondas y el ganador, para luego agruparlas en la lista marcador
# Proceso: Se recorren las jugadas de los jugadores y se determina el ganador de cada ronda  
def ganadorRondas(jugadaP1, jugadaP2):
    ganaJu1 = "Jugador 1 gana"
    ganaJu2 = "Jugador 2 gana"
    empate = "Empate"
    #Tomaremos en consideracion que piedra(R) gana a tijera(S), tijera(S) gana a papel(P) y papel gana a piedra(R)

    #Si la jugada del jugador 1 es igual a la del jugador 2, se imprime empate
    if jugadaP1 == jugadaP2:
        #Le retornamos empate a la función juego_piedra_papel_tijera
        return empate
    #Si la jugada del jugador 1 es igual a piedra y el jugador 2 saco papel, gana el jugador 2
    elif jugadaP1 == "R" and jugadaP2 == "P":
        #Le retornamos ganaJu2 a la función juego_piedra_papel_tijera
        return ganaJu2
    #Si la jugada del jugador 1 es igual a piedra y el jugador 2 saco tijera, gana el jugador 1
    elif jugadaP1 == "R" and jugadaP2 == "S":
        #Le retornamos ganaJu1 a la función juego_piedra_papel_tijera
        return ganaJu1
    #Si la jugada del jugador 1 es igual a papel y el jugador 2 saco piedra, gana el jugador 1
    elif jugadaP1 == "P" and jugadaP2 == "R":
        #Le retornamos ganaJu1 a la función juego_piedra_papel_tijera
        return ganaJu1
    #Si la jugada del jugador 1 es igual a papel y el jugador 2 saco tijera, gana el jugador 2
    elif jugadaP1 == "P" and jugadaP2 == "S":
        #Le retornamos ganaJu2 a la función juego_piedra_papel_tijera
        return ganaJu2
    #Si la jugada del jugador 1 es igual a tijera y el jugador 2 saco piedra, gana el jugador 2
    elif jugadaP1 == "S" and jugadaP2 == "R":
        #Le retornamos ganaJu2 a la función juego_piedra_papel_tijera
        return ganaJu2
    #Si la jugada del jugador 1 es igual a tijera y el jugador 2 saco papel, gana el jugador 1
    elif jugadaP1 == "S" and jugadaP2 == "P":
        #Le retornamos ganaJu1 a la función juego_piedra_papel_tijera
        return ganaJu1

#El juego main
#Entrada: Recibe los movimientos de los jugadores
#Salida: Imprime el resultado si gano X jugador o fue empate
#Proceso: Se recorren las jugadas de cada jugador en su respectivo arreglo y se determina el ganador de cada ronda
def juego_piedra_papel_tijera(movimientos):
    #Inicializamos los contadores de victorias
    contadorVicJugador1 = 0
    contadorVicJugador2 = 0
    seEmpato = 0
    jugadasP1 = movimientos.get("jugador1", [])
    jugadasP2 = movimientos.get("jugador2", [])

    jugadas = 5
    # Marcador será una lista que guardara los resultados de las rondas
    marcador = []
    #Se recorre las jugadas de los jugadores para determinar el ganador y se van mandando a la función ganadorRondas
    while jugadas > 0:
        jugadaP1 = jugadasP1.pop(0)
        jugadaP2 = jugadasP2.pop(0)
        marcador.append(ganadorRondas(jugadaP1, jugadaP2))
        jugadas -= 1
    #Se recorre la lista marcador para determinar el ganador de las rondas
    for mov in marcador:
        if mov == "Jugador 1 gana":
            contadorVicJugador1 += 1
        elif mov == "Jugador 2 gana":
            contadorVicJugador2 += 1
        else:
            seEmpato += 1
    #Se imprime el resultado de las rondas
    print("El Jugador 1 gano un total de: ", contadorVicJugador1)
    print("El Jugador 2 gano un total de: ", contadorVicJugador2)
    print("Empates:", seEmpato)
    #Se determina el ganador de las rondas
    if contadorVicJugador1 > contadorVicJugador2:
        print("Jugador 1 gana")
    elif contadorVicJugador1 < contadorVicJugador2:
        print("Jugador 2 gana")
    else:
        print("Fue un Empate!")


# Diccionario JSON con las jugadas de los jugadores
jugadas = {
    "jugador1": ["R", "P", "P", "S", "R"],
    "jugador2": ["P", "P", "P", "R", "P"]
}
# Le mandamos las jugadas a la función

if __name__ == "__main__":
    juego_piedra_papel_tijera(jugadas)
