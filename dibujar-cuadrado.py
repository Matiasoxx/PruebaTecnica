#Ejercicio 2: Cree una función que, dado un número entero permita dibujar un cuadrado utilizando la letra O


#Funcion para dibujar un cuadrado
#Entrada: Se recibira un número entreo que permitira dibujar un cuadrado dejando el centro vacio calcando unicamente los lados. Si es un cuadrado 
#         y el usuario indica un número de 1, se dibujara un cuadrado de 1x1, si es de 2x2. Si es de 3x3 se deja vacio el centro.
#         Es decir, necesitaremos contar con un ciclo para las filas y otro ciclo para las columnas.
#Salida: Se va a mostrar en pantalla el cuadrado dibujado con los respectivvos lados solicitados.

def dibujar_cuadrado(numero):
    #Primeramente tomamos en consideracion que el cuadrado se dibujara con una letra en especifico. En este caso la letra O.
    dibujo = "O"
    #Ciclo para dibujar el cuadrado con los respectivos lados solicitados
    #Realizamos un ciclo para dibujar el cuadrado controla las filas
    for i in range(numero):
        #Ciclo para controlar las columnas
        for j in range(numero):
            #Manejamos si estamos en la primera fila o ultima fila o primera columna o ultima columna
            if i == 0 or i == numero-1 or j== 0 or j == numero-1:
                print(dibujo, end=" ")
            else:
                print(" ", end=" ")
        print()

#Main
if __name__ == "__main__":
    #Se pide al usuario que ingrese un número entero arrojando error en caso de que no sea un número entero
    numero = int(input("Ingrese un número entero: "))
    #Se manda a llamar a la función dibujar_cuadrado
    dibujar_cuadrado(numero)