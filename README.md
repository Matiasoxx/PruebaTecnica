# Soluciones a Pruebas Técnicas en Python.

Este repositorio contiene las soluciones a una serie de pruebas técnicas resueltas en Python. A continuación se describen los ejercicios planteados y cómo se implementaron las soluciones.
## Tabla de Contenidos
- [Ejercicio 1: Jugador de ajedrez (No resuelto)](##ejercicio-1-jugador-de-ajedrez)
- [Ejercicio 2: Cuadrado de lados "O"](##ejercicio-2-cuadrado-de-lados-o)
- [Ejercicio 3: Verificar función equilibrada](##ejercicio-3-verificar-función-equilibrada)
- [Ejercicio 4: Piedra (R), Papel (P) o Tijera (S)](##ejercicio-4-piedra-r-papel-p-o-tijera-s)

## Instalación y Ejecución

**1. Clona el repositorio:**
   ```bash
   git clone https://github.com/Matiasoxx/PruebaTecnica.git
   ```
**2. Navega al directorio del proyecto:**
 	``` cd PruebaTecnica ```
	
**3. Ejecuta los scripts según el ejercicio que desees probar:**

   - **Ejercicio 2:**
     ```bash
     python dibujar-cuadrado.py
     ```

   - **Ejercicio 3:**
     ```bash
     python validar-funcion-equilibrada.py
     ```

   - **Ejercicio 4:**
     ```bash
     python piedra-papel-tijeras.py
     ```

# Ejercicio 1: Jugador de ajedrez (No resuelto).
Un jugador de ajedrez requiere una función que le permita saber si dado un tablero de ajedrez de entrada (8x8) puede determinar si al mover de posición un peón este:

- a) Peón Captura a otro Peón (debe retornar el tablero con la nueva posición)
- b) Movimiento no válido (debe retornar el tablero de entrada sin alterar e indicar que el movimiento no es válido)
- c) Movimiento válido (debe retornar el tablero con la nueva posición)

Nota: El tablero sólo cuenta con 8 peones por jugador.

#### Estado del Ejercicio y Contribución
Este ejercicio aún no está resuelto. Los problemas que enfrenté incluyen:

- La lógica para determinar si un peón captura otro peón en base a la posición en el tablero.
- Manejar correctamente los movimientos válidos del peón dentro de las reglas del ajedrez.

Si alguien tiene una solución para este problema, se agradecen las contribuciones. Por favor, abre un Pull Request con tu propuesta.

# Ejercicio 2: Cuadrado de lados "O".
Cree una función que, dado un número entero permita dibujar un cuadrado utilizando la letra O.
Se requiere:
- a) Explicar los parámetros de entrada
- b) Explicar los parámetros de salida
- c) Una breve descripción de la lógica que utilizará para resolver el problema
- d) Satisfacer el requerimiento

Ejemplo: Lado 4.

![image](https://github.com/user-attachments/assets/b649011d-7aa7-41a4-95af-019f507add02)

# Ejercicio 3: Verificar función equilibrada.
Cree una función que permita validar que una expresión con paréntesis, llaves y corchetes se encuentra equilibrada (significa que paréntesis, llaves y corchetes de una expresión se abren y cierran en orden de forma correcta)

Ejemplo: 
	
  Expresión equilibrada: `{ [ a * ( c + d ) ] – b }`
 
  Expresión no equilibrada: `{ a * ( c + d ) ] – b }`


Se requiere:
- a) Explicar los parámetros de entrada
- b) Explicar los parámetros de salida
- c) Una breve descripción de la lógica que utilizará para resolver el problema
- d) Satisfacer el requerimiento

# Ejercicio 4: Piedra (R), Papel (P) o Tijera (S)
Se requiere crear una función que permita determinar quién es el ganador de un mejor de 5 (Un jugador requiere de 3 victorias para ganar) para el juego de “Piedra, Papel o Tijera”.

Para resolver este problema se requiere tener en cuenta lo siguiente:

1)	Como entrada se recibirá un objeto JSON con la siguiente estructura
   
```json
{
  "jugador1": ["R", "P", "P", "S", "R"],
  "jugador2": ["P", "P", "P", "R", "P"]
}
```
3)	Para que se pueda comprobar si existe un ganador ambos jugadores deben haber realizado sus 5 jugadas.
4)	Empate es una respuesta valida.
5)	Como respuesta se espera: Victoria Jugador X o Empate.

Se requiere:
- a) Explicar los parámetros de entrada
- b) Explicar los parámetros de salida
- c) Una breve descripción de la lógica que utilizará para resolver el problema
- d) Satisfacer el requerimiento

#### Observación 
El cálculo de quién ganó más rondas (ganadorRondas) podría haber sido implementado utilizando diccionarios para optimizar el tiempo de ejecución. Un diccionario permite acceder a las victorias de cada jugador en tiempo constante, lo que reduce la complejidad en comparación con otras implementaciones como listas o condicionales repetitivos.

### Contribuir
Para contribuir:
1. Haz un fork del repositorio.
2. Crea una rama con la posible solución.
3. Abre un Pull Request y estaré encantado de revisarlo.
