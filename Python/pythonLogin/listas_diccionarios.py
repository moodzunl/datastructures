from funciones_auxiliares import limpiar


def lista_diccionario(id_account):
    # Solicita al usuario que seleccione una acción
    limpiar()
    print("¿Qué te gustaría hacer?")
    print("1. Crear lista")
    print("2. Crear diccionario")
    print("3. Salir")
    choice = input()

    while True:
        # Menú
        if choice == "1":
            limpiar()
            crear_lista(id_account)
            break
        elif choice == "2":
            limpiar()
            crear_diccionario(id_account)
            break
        elif choice == "3":
            limpiar()
            break
        else:
            print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")


def crear_lista(id_account):
    while True:
        lista_input = input("Introduce los elementos de la lista separados por comas: ")
        if not lista_input:
            print("Error: La lista no puede estar vacía.")
            continue

        lista = lista_input.split(",")
        lista = [elem.strip() for elem in lista]
        if not lista:
            print("Error: La lista no puede estar vacía.")
            continue

        listaJoin = ",".join(lista)
        with open("lista.txt", "a") as file:
            file.write(f"{listaJoin}:{id_account}\n")

        print("Lista creada correctamente")
        print(lista)
        print("----------------------------")
        input("Presiona enter para acceder. . . ")
        break


def crear_diccionario(id_account):
    while True:
        diccionario_input = input(
            "Introduce los elementos del diccionario separados por comas (clave:valor): "
        )
        if not diccionario_input:
            print("Error: El diccionario no puede estar vacío.")
            continue

        diccionario = {}
        elementos = diccionario_input.split(",")
        for elemento in elementos:
            if ":" not in elemento:
                print(f"Error: El elemento '{elemento}' no es válido.")
                break

            clave, valor = elemento.split(":")
            clave = clave.strip()
            valor = valor.strip()
            if not clave or not valor:
                print(
                    f"Error: La clave o el valor del elemento '{elemento}' no pueden estar vacíos."
                )
                break

            diccionario[clave] = valor

        else:
            with open("diccionario.txt", "a") as file:
                file.write(f"{diccionario}:{id_account}\n")

            print("Diccionario creado correctamente")
            print(diccionario)
            print("----------------------------")
            input("Presiona enter para acceder. . . ")
            break
