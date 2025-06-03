import math


def convertir_magnitud_a_componentes(magnitud, angulo_grados):
    """
    Convierte un vector expresado en magnitud y ángulo (en grados)
    a sus componentes cartesianas (x, y).

    Parámetros:
    - magnitud (float): longitud del vector.
    - angulo_grados (float): ángulo en grados respecto al eje X positivo.

    Retorna:
    - tuple: (componente_x, componente_y)
    """
    radianes = math.radians(angulo_grados)
    x = magnitud * math.cos(radianes)
    y = magnitud * math.sin(radianes)
    return (x, y)

def sumar_vectores(lista_vectores):
    """
    Suma una lista de vectores representados en componentes cartesianas.

    Parámetros:
    - lista_vectores (list): lista de tuplas (x, y) representando vectores.

    Retorna:
    - tuple: vector resultante (x_total, y_total)
    """
    suma_x = sum(vector[0] for vector in lista_vectores)
    suma_y = sum(vector[1] for vector in lista_vectores)
    return (suma_x, suma_y)
