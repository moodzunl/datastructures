from funciones_auxiliares import limpiar

arrays = []


def quick_sort(arr):
    if len(arr) <= 1:
        return arr, 0, 0

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    left_sorted, left_swaps, left_comparisons = quick_sort(left)
    right_sorted, right_swaps, right_comparisons = quick_sort(right)

    swaps = left_swaps + right_swaps + len(left) + len(right)
    comparisons = left_comparisons + right_comparisons + len(arr) - len(middle)

    return left_sorted + middle + right_sorted, swaps, comparisons


def bubble_sort(arr):
    n = len(arr)
    swaps = 0
    comparisons = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return arr, swaps, comparisons


def insert_sort(arr):
    swaps = 0
    comparisons = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparisons += 1
            arr[j + 1] = arr[j]
            j -= 1
            swaps += 1
        arr[j + 1] = key
    return arr, swaps, comparisons


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left_sorted, left_swaps, left_comparisons = merge_sort(left)
        right_sorted, right_swaps, right_comparisons = merge_sort(right)

        swaps = left_swaps + right_swaps
        comparisons = left_comparisons + right_comparisons

        i = j = k = 0
        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        return arr, swaps, comparisons
    else:
        return arr, 0, 0


def selection_sort(arr):
    swaps = 0
    comparisons = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[min_idx] > arr[j]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return arr, swaps, comparisons


def conseguir_datos(id_account):
    # Leer el archivo de texto y agregar los IDs existentes a la lista
    try:
        with open("lista.txt", "r") as file:
            for line in file:
                fields = line.strip().split(":")
                if fields[1] == id_account:
                    arrays.append(list(map(int, fields[0].split(","))))
            for i, array in enumerate(arrays):
                print(f"{i+1}. {array}")

            print("Selecciona el arreglo que deseas ordenar")
            choice = int(input())

            array_seleccionado = arrays[choice - 1].copy()

            print("Selecciona el tipo de ordenamiento que deseas aplicar:")
            print("1. QuickSort")
            print("2. BubbleSort")
            print("3. InsertSort")
            print("4. MergeSort")
            print("5. SelectionSort")

            ordenamiento = int(input())

            if ordenamiento == 1:
                array_ordenado, swaps, comparisons = quick_sort(array_seleccionado)
            elif ordenamiento == 2:
                array_ordenado, swaps, comparisons = bubble_sort(array_seleccionado)
            elif ordenamiento == 3:
                array_ordenado, swaps, comparisons = insert_sort(array_seleccionado)
            elif ordenamiento == 4:
                array_ordenado, swaps, comparisons = merge_sort(array_seleccionado)
            elif ordenamiento == 5:
                array_ordenado, swaps, comparisons = selection_sort(array_seleccionado)
            else:
                print("Opción inválida.")
                return

            print(f"Arreglo ordenado: {array_ordenado}")
            print(f"Intercambios realizados: {swaps}")
            print(f"Comparaciones realizadas: {comparisons}")

    except FileNotFoundError:
        print("\n")
        print("El archivo no se encontró")
        input("Presiona enter para continuar. . .")
        input()
