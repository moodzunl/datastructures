import time


def quicksort(arr, inicio, fin):
    if inicio < fin:
        pivot = particion(arr, inicio, fin)
        quicksort(arr, inicio, pivot - 1)
        quicksort(arr, pivot + 1, fin)


def particion(arr, inicio, fin):
    pivot = arr[fin]
    i = inicio - 1
    comparaciones = 0
    intercambios = 0

    for j in range(inicio, fin):
        comparaciones += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            intercambios += 1
            print(f"Intercambio {arr[j]} con {arr[i]}")
            print(f"Array actual: {arr}")
            print("-----------------------------")
            time.sleep(1)

    arr[i + 1], arr[fin] = arr[fin], arr[i + 1]
    intercambios += 1
    print(f"Intercambio {arr[fin]} con {arr[i + 1]}")
    print(f"Array actual: {arr}")
    print(f"Comparaciones realizadas: {comparaciones}")
    print(f"Intercambios realizados: {intercambios}\n")
    print("-----------------------------")
    time.sleep(1)

    return i + 1
