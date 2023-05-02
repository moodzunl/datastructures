from funciones_auxiliares import limpiar

arrays = []


def metodos_ordenamiento(id_account):
    while True:
        limpiar()
        print("¿Qué te gustaría hacer?")
        print("1. Ordenamiento quicksort")
        opcion = input()

        if opcion == "1":
            conseguir_datos(id_account)


def conseguir_datos(id_account):
    # Leer el archivo de texto y agregar los IDs existentes a la lista
    try:
        limpiar()
        with open("lista.txt", "r") as file:
            for line in file:
                fields = line.strip().split(":")
                if fields[1] == id_account:
                    arrays.append(fields[0])
            for i, array in enumerate(arrays):
                print(f"{i+1}. {array}")

            print("Selecciona el arreglo que deseas ordenar")
            choice = input()
            if choice == "1":
                quicksort(arrays[0], 0, len(arrays[0]) - 1)
                print("Presiona enter para continuar. . .")
                input()

    except FileNotFoundError:
        print("\n")
        print("El archivo no se encontró")
        input("Presiona enter para continuar. . .")


def quicksort(arr, low, high):
    if low < high:
        # Encuentra el índice del pivote
        pivot_index = (low + high) // 2
        pivot_value = arr[pivot_index]

        # Mueve el pivote al final del arreglo
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        # Inicializa los índices de los elementos menores y mayores
        i = low - 1
        j = low

        # Recorre el arreglo y mueve los elementos menores que el pivote a la izquierda
        while j < high:
            # Incrementa el índice de los elementos menores
            if arr[j] < pivot_value:
                i += 1
                # Realiza el intercambio
                arr[i], arr[j] = arr[j], arr[i]
                # Imprime el intercambio
                print(f"Intercambio: {arr[i]} <--> {arr[j]}")

            # Incrementa el índice de los elementos revisados
            j += 1
            # Imprime la comparación
            print(f"Comparación: {arr[j-1]} vs {pivot_value}")

        # Mueve el pivote a la posición correcta
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        # Imprime el intercambio
        print(f"Intercambio: {arr[i+1]} <--> {arr[high]}")

        # Recursivamente ordena los subarreglos
        quicksort(arr, low, i)
        quicksort(arr, i + 2, high)
