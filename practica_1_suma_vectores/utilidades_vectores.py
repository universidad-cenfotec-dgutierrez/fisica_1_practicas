from calculos_vectores import convertir_magnitud_a_componentes
from metodo_ingreso import MetodoIngresoVector 

def obtener_lista_vectores(n):
    """
    Solicita al usuario el método de ingreso (componentes o magnitud/dirección)
    y retorna el vector correspondiente en formato (x, y).

    Retorna:
    - tuple: vector en componentes cartesianas
    """
    vectores = []
    for i in range(n):
        print(f"\n--- Vector #{i + 1} ---")
        vector = ingresar_vector()
        vectores.append(vector)
    return vectores

def ingresar_vector():
    """
    Solicita al usuario el método de ingreso (componentes o magnitud/dirección)
    y retorna el vector correspondiente en formato (x, y).

    Retorna:
    - tuple: vector en componentes cartesianas
    """
    print("\nSeleccione el tipo de ingreso del vector:")
    print("1. Por componentes (x, y)")
    print("2. Por magnitud y dirección (en grados)")
    
    while True:
        opcion = input("Opción (1 o 2): ").strip()
        if opcion == MetodoIngresoVector.COMPONENTES.value:
            return ingresar_por_componentes()
        elif opcion == MetodoIngresoVector.MAGNITUD_DIRECCION.value:
            return ingresar_por_magnitud_y_direccion()
        else:
            print("Opción inválida. Intente de nuevo.")

def ingresar_por_componentes():
    """
    Solicita al usuario las componentes x y y del vector,
    validando que sean números y mostrando ejemplos.

    Retorna:
    - tuple: (x, y)
    """
    print("Formato esperado: solo números. Ejemplo válido: 3.5 o -2")
    
    while True:
        try:
            x = float(input("Ingrese la componente x del vector (ej: 2.5): "))
            y = float(input("Ingrese la componente y del vector (ej: -1): "))
            return (x, y)
        except ValueError:
            print("Entrada inválida. Ingrese solo números, sin paréntesis ni comas. Intente de nuevo.\n")

def ingresar_por_magnitud_y_direccion():
    """
    Solicita al usuario la magnitud y dirección del vector,
    mostrando un ejemplo de entrada válida.

    Retorna:
    - tuple: (x, y)
    """
    print("Formato esperado: números reales. Ejemplo válido: Magnitud: 5  Ángulo: 45")
    
    while True:
        try:
            magnitud = float(input("Ingrese la magnitud del vector (ej: 5.0): "))
            angulo = float(input("Ingrese el ángulo en grados (ej: 30): "))
            return convertir_magnitud_a_componentes(magnitud, angulo)
        except ValueError:
            print("Entrada inválida. Ingrese solo números reales, sin símbolos extra. Intente de nuevo.\n")

