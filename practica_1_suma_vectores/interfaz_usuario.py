def mostrar_menu():
    """
    Muestra el menú de introducción del programa al usuario.
    """
    print("==== SUMA DE VECTORES ====")
    print("Este programa permite sumar N vectores.")
    print("Puede ingresarlos por componentes o por magnitud y dirección.")
    print()

def obtener_numero_vectores():
    """
    Solicita al usuario el número de vectores que desea sumar.
    Valida que sea un entero mayor o igual a 2.

    Retorna:
    - int: cantidad de vectores
    """
    while True:
        try:
            cantidad = int(input("¿Cuántos vectores desea sumar? "))
            if cantidad < 2:
                print("Debe ingresar al menos 2 vectores para realizar una suma.")
            else:
                return cantidad
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def imprimir_resultado(vector_resultante):
    """
    Imprime el vector resultante de la suma en formato de componentes.

    Parámetros:
    - vector_resultante (tuple): resultado de la suma (x, y)
    """
    x, y = vector_resultante
    print("\n=== RESULTADO FINAL ===")
    print(f"Vector resultante (en componentes):")
    print(f"X = {x:.2f}")
    print(f"Y = {y:.2f}")
