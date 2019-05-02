# tsp
Solution of Traveling Salesman Problem.


### Algoritmo
----
desarrollado con python y utilizando archivos csv para obtener la data necesaria.

  1. abrimos el archivo csv dado y obtenemos un nuevo archivo con los campos necesarios y segun una region
  2. guardo los datos de cada localidad en un diccionario 
  3. luego obtengo una lista de adyacencia con pesos de ese diccionario
  4. se le aplica el algoritmo ucs estudiado en clase
  5. obtengo las localidades recorridas de incio a fin y los pesos de los caminos tomados.

Fuentes:
- [Algoritmo de costo uniforme (UCS)](https://es.coursera.org/lecture/resolucion-busqueda/algoritmo-de-costo-uniforme-ucs-W4vmS)
- [Uniform-cost search (UCS)](https://mhesham.wordpress.com/2010/04/08/problem-solving-techniques-part2/)
