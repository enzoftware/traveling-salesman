<img src="https://cdn-images-1.medium.com/max/1600/1*by3MgdkmamEAxlCaIH68Xg.jpeg" height="350px" align="center"/>

# Trabajo Parcial: Traveling Salesman Problem
---
## Integrantes:
- Enzo Lizama Paredes (u201618965)
- Miguel Delgado Castillo (u201615527)

## Introduccion:

:thinking: : "Dada una lista de ciudades y las distancias entre cada par de ciudades, ¿cuál es la ruta más corta posible que visita cada ciudad y regresa a la ciudad de origen?"

El dataset a ser utilizado en este trabajo es el listado de centros poblados del Perú. El dataset contiene la
posición geográfica (latitud y longitud) de cada centro poblado del país.

## Objetivos :

Encontrar una solucion al problema previamente descrito con alguna de las siguientes estrategias vistas durante clase.
- Fuerza bruta
- Backtracking
- BFS
- DFS

## Marco teorico:

El problema del vendedor que viaja describe a un vendedor que debe viajar entre N ciudades. El orden en el que lo hace es algo que no le importa, siempre que visite cada una de ellas durante su viaje y termine donde estaba al principio. Cada ciudad está conectada a otras cercanas por ciudades, o nodos, por aviones, por carretera o ferrocarril. Cada uno de esos enlaces entre las ciudades tiene uno o más pesos (o el costo) adjuntos. El costo describe cuán "difícil" es atravesar este borde en el gráfico, y puede darse, por ejemplo, por el costo de un boleto de avión o boleto de tren, o quizás por la longitud del borde, o el tiempo requerido para completar el recorrido. El vendedor desea mantener tanto los costos de viaje como la distancia que recorre lo más bajo posible.

#### Vocabulario para el proyecto:

- **Un conjunto de ciudades:** necesitaremos representar un conjunto de ciudades; El tipo de datos ```set``` de Python podría ser apropiado.
- **Distancia entre cada par de ciudades:** Si ```A``` y ```B``` son ciudades, esta podría ser una función, ```distancia (A, B)``` o una búsqueda de tabla, ```distancia [A] [B]```. La distancia resultante será un número real.
- **Ciudad:** Todo lo que tenemos que saber sobre una ciudad individual es cuán lejos está de otras ciudades. No tenemos que saber su nombre, población, mejores restaurantes o cualquier otra cosa. Por lo tanto, una ciudad podría ser solo un número entero (0, 1, 2, ...) utilizado como índice en una tabla de distancias, o una ciudad podría ser un par de coordenadas (x, y), si estamos usando la línea recta distancia en un avion
- **Tour:** Un tour es un orden específico para visitar las ciudades; En Python los tipos de datos de ```list``` o ```tuple``` funcionarían. Por ejemplo, dado el conjunto de ciudades ```{A, B, C, D}```, un recorrido puede ser la lista ```[B, D, A, C]```, lo que significa viajar de B a D a A a C y finalmente regresar a B.
- **Recorrido más corto posible:** el recorrido más corto es aquel cuya duración del recorrido es el mínimo de todos los recorridos.
- **Duración del recorrido:** la suma de las distancias entre las ciudades adyacentes en el recorrido (incluida la última ciudad de regreso a la primera ciudad). Probablemente una función, ```tour_length (tour)```.
- **¿Qué es ...?** Podemos definir una función para responder la pregunta ¿cuál es el recorrido más corto posible? La función toma un conjunto de ciudades como entrada y devuelve un recorrido como salida. Usaré la convención de que cualquier función de este tipo tendrá un nombre que termina en las letras ```tsp```, la abreviatura tradicional de Problema de vendedor ambulante.

## Analisis:

Cada una de las soluciones estara separada en una rama distinta con los pasos para poder compilar el proyecto y el analisis de cada una de las implementaciones.

- [Solucion backtracking](https://github.com/enzoftware/tsp/tree/feature/backtrackingSolution)
- [Solucion ucs](https://github.com/enzoftware/tsp/tree/feature/ucs_solution)
- [Solucion dynamic programming](https://github.com/enzoftware/tsp/tree/feature/dynamic-programming-solution)
- [Solucion kruskal](https://github.com/enzoftware/tsp/tree/feature/kruskal-solution)

## Conlusiones:

Al finalizar el trabajo se concluye que ninguno de los algoritmos propuestos es el indicado para resolver el TSP, es preciso indicar que las implementaciones desarrolladas han sido limitadas por el tipo de algoritmos que se podian utilizar. 
