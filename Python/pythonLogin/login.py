from funciones_auxiliares import limpiar
from listas_diccionarios import lista_diccionario
from ordenamientos import conseguir_datos
from arboles import tipos_arboles


# Bucle de ejecución
def logged(id_account):
    while True:
        # Solicita al usuario que seleccione una acción
        limpiar()
        print("¿Qué te gustaría hacer?")
        print("1. Crear lista o diccionario")
        print("2. Metodos de ordenamiento")
        print("3. Tipos de arboles binarios")
        print("4. Salir")
        choice = input()

        # Menú
        if choice == "1":
            limpiar()
            lista_diccionario(id_account)
        elif choice == "2":
            limpiar()
            conseguir_datos(id_account)
        elif choice == "3":
            tipos_arboles(id_account)
            limpiar()
        elif choice == "4":
            limpiar()
            break
        else:
            print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")
