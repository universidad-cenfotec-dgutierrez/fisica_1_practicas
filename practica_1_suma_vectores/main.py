from interfaz_usuario import mostrar_menu, obtener_numero_vectores, imprimir_resultado
from utilidades_vectores import obtener_lista_vectores
from calculos_vectores import sumar_vectores

def main():
    mostrar_menu()
    n = obtener_numero_vectores()
    vectores = obtener_lista_vectores(n)
    resultado = sumar_vectores(vectores)
    imprimir_resultado(resultado)

if __name__ == "__main__":
    main()
