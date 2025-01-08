# Modelo Predador-Presa
Este es un modelo No Lineal, que usa ecuaciones de Lotka-Volterra,
donde se estudian/visualizan los cambios de 2 poblaciones distintas a lo largo del tiempo
(distintas generaciones).

### Nuestros protagonistas:
- dX -> diferencial o cambio de conejos --> dX = r1 * X - P * X * Y 
- dY -> diferencial o cambio de zorros --> dY =  a * P * X * Y - r2 * Y
- P : el coeficiente de probabilidad de caza (0< P <1); 
- r1 : con la tasa de crecimiento intrínseco de conejos, 
- r2 : tasa de mortalidad de los zorros (en ausencia de conejos)
- a : tasa de nacimiento de zorros por cada conejo cazado.
-----
#### Entorno:
Se parte de que hay dos poblaciones: una de zorros y otra de conejos.
 - Ambiente: campo cerrado natural, donde no intervienen otros animales ni predadores.
 - Sin zorros => 
   + los conejos se multiplican, hasta que el campo agote su capacidad de alimento. 
Superado este límite los conejos se mueren de hambre y la población se estabiliza (eso es con la ec. Logística).
 - Sin liebres => 
   + los zorros no tendrían alimento, pueden sobrevivir hasta morir de hambre.
 - Si coexisten ambas poblaciones => 
   + los zorros se alimentan de los conejos y se multiplican. 
Pero hasta un punto donde: si la población de zorros es muy numerosa no alcanzarán los conejos para todos y comienzan a morir de hambre. 
 - Así, ambas poblaciones se estabilizan. Van osilando: una crece cuando la otra decrece y así...
----
#### Características del sistema:
 - Al ser un sistema NO Lineal, su comportamiento dependerá mucho de la cantidad de zorros y conejos iniciales.
 - También influyen las tasa de natalidad y mortalidad de cada especie.
 - Si se hiciera un analisis de sensibilidad, se vería que un cambio en cualquier factor, puede generar repercusiones en los resultados
 - Las ecuaciones de Lotka-Volterra en su estado original No tienen una capacidad de carga fija como una Ecuación Logística de 1 sola población. \
   - Se le pueden definir puntos de Equilibrio.

#### Puntos de Equilibrio: 
 Es donde dX y dY deberían ser =0; o sea, la velocidad de cambio es 0 \
 punto donde ambas poblaciones deberían mantenerse estables
- Xe = r2 / a*P
- Ye = r1 / P \
Esos puntos se obtienen al buscar las raíces dX y dY.
------
#### Ecuación Logística de L-V:
- Acá la idea es añadir una regla de entorno, sobre todo para los conejos que no tienen límite de crecimiento.
- Con la Ec. Logística: se hace que el crecimiento de la población sea proporcional a su tamaño actual,
y que además se estabilice cuando alcanza una capacidad de carga.
- Solo hace falta modificar la de los conejos, porque los Zorros ya dependen de ellos:
  - conejos: x' = r1 * x − k * x^2 − p * x * y
- Notese el añadido del parámetro Cuadrático:  − k * x^2
- Con esto, la gráfica debería verse como oscila hasta ir convergiendo en los puntos de Equilibrio.
-----
#### Ruido:
+ Se introducen factores de ruido en algunas partes del código, para que el modelo sea estocástico, 
ya que esa aleatoriedad lo hace más parecido a las anomalías que pueden darse en la realidad.
  + Estocástico: tiene incertidumbre, usa probabilidad.
  + Determinístico: es predecible, se rige con leyes matemáticas
+ Sirve para evaluar la sensibilidad de cada parámetro (la entrada de información al sistema) y ver como afecta a 
las variables/poblaciones.
----
- Este código está lleno de "scaffolding", ese código intermedio en los #
- Lo debería sacar, pero es más facil y menos confuso tenerlo ahí para hacer comparaciones rápidas
-----
- Si hubiera una tabla con estadísticas históricas, se podrían calcular los valores de alfa, beta, etc...
con compute_rel_diff.
- Esa función calcula las diferencias relativas entre los elementos de un iterable. Que en este caso sería la diferencia
entre los valores historicos de un parámetro medido.
- Entonces se podría hacer un barrido con los parámetros calculados de esa forma.
- Sumado al ruido random, por ahí puede servir para tratar de predecir valores futuros.
- ----

## Revisar el archivo "Resultados-graficos.md" para más información
Los resultados son extraidos de los archivos:
- L-V_calculo_manual.py

y
- L-V_automático.py