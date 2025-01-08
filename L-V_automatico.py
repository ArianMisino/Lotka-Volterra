# A sword day! A red day! Ere the Sun rises... forth Eorlingas!!
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import random


def ecu_logistica(con_ini, t, r1, p, r2, a, k):
    """ para ecuaciones logísticas:
        conejos: x' = r1.x − k.x^2 − p.x.y
        zorros: y' = a.p.x.y − r2.y
        para gráficas de elongación y fase atenuadas"""
    dx = r1 * con_ini[0] - k * con_ini[0] ** 2 - p * con_ini[0] * con_ini[1]
    # Nótese que la ecuación de Zorros queda igual, esto es porque su supervivencia ya está liagada a los conejos
    # dy = - r2 * con_ini[1] + a * con_ini[0] * con_ini[1] * p
    dy = - r2 * con_ini[1] + a * con_ini[0] * con_ini[1]
    # la bendita p es la personificación de la fealdad gráfica

    return np.array([dx, dy])

if __name__ == "__main__":
    """Estudio del model Predador-Presa, usando ecuaciones de Lotka-Volterra y variaciones"""
    # Definiendo parámetros:
    r1 = 1  # nacimiento de conejos
    p = 0.1  # probabilidad de 1 conejo sea cazado x 1 zorro: 0 < p < 1
    p_random = random.uniform(0.01, 0.99)  # acá se genera 1 vez, pero distinto para cada run
    r2 = 0.5  # mortalidad Depredadores
    a = 0.02  # Crecimiento Depredadores
    # Condiciones iniciales
    x0 = 40  # Presas / Conejos
    y0 = 20  # Depredadores / Zorros
    # puntos de equilibrio: (se pueden usar estas como poblaciones iniciales)
    # x_equil = r2 / (p * a)
    x_equil = r2 / a
    y_equil = r1 / p
    print("esto es pto equilibrio en x: ", x_equil)
    print("esto es pto equilibrio en y: ", y_equil)
    # amplitud del término de ruido: el multiplicador, para ver qué tanto molesta digamos

    conds_iniciales = np.array([x0, y0])
    # conds_iniciales = np.array([x_equil, y_equil])

    # Condiciones para integración que va a usar el odeint
    tf = 200
    N = 800
    t_0 = 0
    # esto devuelve un arreglo t que empieza en t_0, termina en tf, y está div en intervalos según N,
    # o sea, para este caso particular, va incrementando de a 0.25, porque 200/800 = 0.25
    t = np.linspace(0, tf, N)
    """print("esto es t: ")
    print(t)
    print("eso fue t ")"""

    # sigamos con el menjunje de la cuestión:
    """Ahora viene la parte para optimizar el modelo, porque hasta este punto, no se tienen en cuenta:
        - no hay limitaciones del entorno
        - o sobre la Capacidad de Carga
        Acá se le va a dar un comportamiento Logístico poniendo un parámetro adicional cuadrático.
        Como la supervivencia de los Zorros está dada según los Conejos, solo debemos modificar esa ecuación"""
    # agregamos la constante k para el parámetro Cuadrático:
    k = 0.001  # no encontré una fórmula que la defina como en el caso de h
    # hacemos una nueva variable solución, porque esencialmente ha cambiado el sistema:
    solucion_logistic = odeint(ecu_logistica, conds_iniciales, t, args=(r1, p, r2, a, k))

    # Gráfico Poblacional Logístico
    plt.grid()
    plt.plot(t, solucion_logistic[:, 0], 'b-', label='Conejos')
    plt.plot(t, solucion_logistic[:, 1], 'r-', label='Zorros')
    plt.legend()
    plt.xlabel('t', fontsize=12)
    plt.ylabel('poblaciones X e Y', fontsize=12)
    plt.title('Grafico de Elongación Lotka-Volterra Logístico')
    plt.show()

    # Gráfico Poblacional Logístico de Zorros
    plt.grid()
    plt.plot(t, solucion_logistic[:, 1])
    plt.xlabel('Tiempo')
    plt.ylabel('Tamaño de Población de Zorros')
    plt.legend('Zorros')
    plt.title('Lotka-Volterra Logístico - Zorro Edition')
    plt.show()

    # Gráfico de Fase Logístico
    plt.grid()
    plt.plot(solucion_logistic[:, 0], solucion_logistic[:, 1], lw=2, alpha=0.8)
    plt.plot(x_equil, y_equil, marker="o", markersize=6, markeredgecolor="orange", markerfacecolor="blue")
    plt.xlabel('Conejos x', fontsize=12)
    plt.ylabel('Zorros y', fontsize=12)
    plt.title('Grafico de Fase Lotka-Volterra Logístico')
    plt.show()
