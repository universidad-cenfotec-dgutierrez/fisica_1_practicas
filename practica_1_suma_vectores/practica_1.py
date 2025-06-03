import math

def mostrar_menu():
    print("==== PRACTICA #1 SUMA DE VECTORES ====")
    print("Este programa permite sumar N vectores.")
    print("Puede ingresarlos por componentes o por magnitud y dirección.")
    print()

def obtener_numero_vectores():
    while True:
        try:
            cantidad = int(input("¿Cuántos vectores desea sumar? "))
            if cantidad < 1:
                print("Por favor, ingrese un número mayor que cero.")
            else:
                return cantidad
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def ingresar_vector():
    print("\nSeleccione el tipo de ingreso del vector:")
    print("1. Por componentes (x, y)")
    print("2. Por magnitud y dirección (en grados)")
    
    while True:
        opcion = input("Opción (1 o 2): ").strip()
        if opcion == "1":
            return ingresar_por_componentes()
        elif opcion == "2":
            return ingresar_por_magnitud_y_direccion()
        else:
            print("Opción inválida. Intente de nuevo.")

def ingresar_por_componentes():
    x = float(input("Ingrese la componente x: "))
    y = float(input("Ingrese la componente y: "))
    return (x, y)

def ingresar_por_magnitud_y_direccion():
    magnitud = float(input("Ingrese la magnitud del vector: "))
    angulo = float(input("Ingrese el ángulo en grados (desde el eje x): "))
    radianes = math.radians(angulo)
    x = magnitud * math.cos(radianes)
    y = magnitud * math.sin(radianes)
    return (x, y)

def sumar_vectores(lista_vectores):
    suma_x = sum(vector[0] for vector in lista_vectores)
    suma_y = sum(vector[1] for vector in lista_vectores)
    return (suma_x, suma_y)

def imprimir_resultado(vector_resultante):
    x, y = vector_resultante
    print("\n=== RESULTADO FINAL ===")
    print(f"Vector resultante (en componentes):")
    print(f"X = {x:.2f}")
    print(f"Y = {y:.2f}")

def main():
    mostrar_menu()
    n = obtener_numero_vectores()
    vectores = []

    for i in range(n):
        print(f"\n--- Vector #{i + 1} ---")
        vector = ingresar_vector()
        vectores.append(vector)

    resultado = sumar_vectores(vectores)
    imprimir_resultado(resultado)

if __name__ == "__main__":
    main()
