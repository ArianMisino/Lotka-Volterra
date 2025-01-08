# A sword day! A red day! Ere the Sun rises... forth Eorlingas!!
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as npy
import random


# Término del ruido para perturbar ec. dif.
def termino_estocastico(amp):
    return amp * random.uniform(-1, 1)


if __name__ == "__main__":

    """" Estudio del model Predador-Presa, usando ecuaciones de Lotka-Volterra
        (se podría hacer un barrido de cada parámetro, pero la funcion de ruido añadido cumple una función similar)"""
    # Definicion de parámetros:
    # timestep: El paso de tiempo que determina la precisión del método de integración de Euler.
    timestep = 0.0001
    # amplitud del término de ruido
    amp = 0.01
    # amp = 0.00
    # tiempo fianl, al llegar ahí, se detiene la simulacion
    end_time = 50

    # crea un vector de tiempo desde 0 hasta end_time, separado por un paso de tiempo "timestep"
    t = npy.arange(0, end_time, timestep)

    # inicializar listas de conejos (x) y zorros (y)
    x = []
    y = []

    # nacimiento de conejos
    r1 = 1
    # mortalidad del conejo o la Probabilidad de que 1 conejo sea cazado x 1 zorro: 0 < p < 1
    p = 0.1
    # muertes de zorros
    r2 = 0.5
    # factor que describe cuántos conejos comidos generan un nuevo zorro // a*P del libro / (alfa * P)
    # a = alfa = Crecimiento/Natalidad de Depredadores
    a = 0.02

    """ Condiciones iniciales para las poblaciones de conejos (x) y zorros (y) en el tiempo = 0 """
    # Normal, poniendo números al azar:
    # x.append(10)  # conejos
    # y.append(5)  # zorros
    # Punto de equilibrio para las poblaciones. Recordemos: p = −α/β // pero acá son 2 pobl que dependen una de la otra
    x.append(r2/a)  # conejos
    y.append(r1/p)  # zorros
    x_equil = r2 / a
    y_equil = r1 / p
    print("esto es pto equilibrio en x: ", x_equil)
    print("esto es pto equilibrio en y: ", y_equil)

    """ Método de integración de Euler Directo"""
    # Se agrega un término de perturbación a los diferenciales para hacer que la simulación sea estocástica.
    for index in range(1, len(t)):
        # Descomentar para añadir estocastimoísmo:
        # r1 = r1 + termino_estocastico(amp) # nacimiento de conejos
        # p = p + termino_estocastico(amp)  # mortalidad del conejo (o probabilidad de cacería)
        # r2 = r2 + termino_estocastico(amp) # Mortalidad de Zorros
        # a = a + termino_estocastico(amp)  # alfa = Nacimiento de Zorros

        """Estas son las ecuaciones de Lotka-Volterra"""
        # evaluar los diferenciales actuales (se aplicó factor común)
        dx = x[index - 1] * (r1 - p * y[index - 1])  # x = r1.x − p.x.y
        dy = -y[index - 1] * (r2 - p * a * x[index - 1])  # y = a.p.x.y − r2.y
        # Uno puede estar tentado a quitar la "p" de la ecuación de "dy", porque parece que los zorros mueren, pero No.
        # La ecuación está bien así, y los zorros no se mueren; solo que el multiplicador se vuelve muy pequeño.
        # Así que, si en el futuro un profesor que tu código está mal, no importa que tan fuertes sen sus argumentos...
        # Confía, y recuérdale que el poder de Jesucristo lo es más

        """Y este es el bendecido método del bendecido Euler"""
        # calculamos el h de euler, o también diferencial de tiempo / xd[]= f(xn,yn)
        # h = (x[index - 1] - x[0]) / index
        # h = x[index] - x[index - 1]  # IndexError: list index out of range
        # he probado con h = 0.5, 1, 0.001 (+-bien), timestep (meh)
        # h = 0.0001  # Funcionó bien para Estocástico con pob iniciales 10 y 5. Pero para inicio en equilibrio NO
        h = 0.0001  # Ahora sí funciona para el Estocástico con iniciales en Equilibrio
        # evaluar el siguiente valor de x e y usando las benditas diferenciales // y[i] = y[i−1] + h.f(x[i−1], y[i−1])
        if amp == 0:
            proximo_x = x[index - 1] + dx * timestep  # timestep = h de euler,
            proximo_y = y[index - 1] + dy * timestep  # o también diferencial de tiempo / xd[]= f(xn,yn)
        else:
            proximo_x = x[index - 1] + dx * h  # timestep = h de euler,
            proximo_y = y[index - 1] + dy * h  # o también diferencial de tiempo / xd[]= f(xn,yn)

        # agregar los próximos valores de X e Y
        # x.append(proximo_x)
        # y.append(proximo_y)
        if amp == 0:
            # add the next value of x and y
            x.append(proximo_x)
            y.append(proximo_y)
        else:
            # agrega ruido a X e Y
            x.append(proximo_x + termino_estocastico(amp))
            y.append(proximo_y + termino_estocastico(amp))

    """ visualization de los resultados """
    if amp == 0:
        # visualización de poblaciones determinísticas contra el tiempo
        plt.grid()
        plt.plot(t, x)
        plt.plot(t, y)
        plt.xlabel('Tiempo')
        plt.ylabel('Tamaño de Población')
        plt.legend(('Conejos', 'Zorros'))
        plt.title('Lotka-Volterra Determinístico')
        plt.show()

        # solo de zorros Determinísticos
        plt.grid()
        plt.plot(t, y)
        plt.xlabel('Tiempo')
        plt.ylabel('Tamaño de Población de Zorros')
        plt.legend('Zorros')
        plt.title('Lotka-Volterra Determinístico - Zorro Edition')
        plt.show()

        # Diagrama de Fase Determinístico
        plt.grid()
        plt.plot(x, y)
        plt.plot(x_equil, y_equil, marker="o", markersize=10, markeredgecolor="orange", markerfacecolor="blue")
        plt.xlabel('Población de Conejos')
        plt.ylabel('Población de Zorros')
        plt.title('Diagrama de Fase de Lotka-Volterra Determinístico')
        plt.show()

    else:
        # visualización de poblaciones estocásticas contra el tiempo
        plt.grid()
        plt.plot(t, x)
        plt.plot(t, y)
        plt.xlabel('Tiempo')
        plt.ylabel('Tamaño de Población')
        plt.legend(('Conejos', 'Zorros'))
        plt.title('Lotka-Volterra Estocástico')
        plt.show()

        # solo de zorros Estocásticos
        plt.grid()
        plt.plot(t, y)
        plt.xlabel('Tiempo')
        plt.ylabel('Tamaño de Población de Zorros')
        plt.legend('Zorros')
        plt.title('Lotka-Volterra Estocástico - Zorro Edition')
        plt.show()

        # Diagrama de Fase estocástico
        plt.grid()
        plt.plot(x, y)
        plt.plot(x_equil, y_equil, marker="o", markersize=10, markeredgecolor="orange", markerfacecolor="blue")
        plt.xlabel('Población de Conejos')
        plt.ylabel('Población de Zorros')
        plt.title('Diagrama de Fase de Lotka-Volterra Estocástico')
        plt.show()

        """# visualización de términos de ruido
        noise = []
        n = []
        for sample in range(100):
            noise.append(termino_estocastico(amp))
            n.append(sample)

        plt.plot(n, noise)
        plt.xlabel('Muestras de ruido arbitrarias')
        plt.ylabel('Ruido')
        plt.title('Perturbación de Natalidad')
        plt.show()"""

