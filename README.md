# Modificaciones realizadas:
### TEMA 1:

##### Ejercicio 3:
Se ha añadido una explicación detallando como se ha obtenido el término $T(\frac{n}{2})$.
##### Ejercicio 7:

Se ha considerado un coste distinto para la función len() de Python, dado que el anterior era erróneo respecto a la documentación del lenguaje.
Se ha calculado correctamente el término $log_2n$, que realmente era $\sqrt{n}$, y se ha añadido una explicación de su razonamiento.

##### Ejercicio 9:

Se ha extendido la documentación explicativa del código.
### TEMA 2:

##### Ejercicio 3:

Se ha añadido un razonamiento sobre distintas estrategias que se puedan tratar para resolver el problema.

Sobre el comentario: "El algoritmo implementado no es correcto porque el número de comparaciones es $> 3\frac{n}{2}$.", ya se razonó en el laboratorio que su número de comparaciones realmente no excedía $3\frac{n}{2}$.

También se ha añadido una explicación detallada de uno de los casos de prueba del problema.

##### Ejercicio 4:

Se ha modificado el programa para que aristas que no existan se consideren aristas de coste infinito.

También se ha añadido una explicación detallada de uno de los casos de prueba del problema.

##### Ejercicio 6:

​	

### TEMA 3:

##### Ejercicio 4:
Se ha extendido y mejorado tanto la descripción del algoritmo, como el paso a paso del caso de prueba, puesto que se pedía ser explicado con mayor claridad.

### TEMA 4:

##### Ejercicio 6:

Se ha corregido un error en el planteamiento y en el código del ejercicio. Los valores de probabilidad se calculaban a base de multiplicar la probabilidad de que un equipo gane, por la probabilidad de que se haya dado la situación del torneo en la que ese equipo tiene un partido ganado menos. Esto se hacía realizando una asignación, sin embargo para situaciones en las que más de un equipo hubiese ganado partidos fallaba, dado que no tenía en cuenta el orden en que pudiese ocurrir las victorias, y calculaba una probabilidad menor. Esto se soluciona, sumando la probabilidad calculada en vez de asignándola.

Asimismo la explicación del algoritmo y el ejemplo recogen este detalle.

### TEMA 5:

