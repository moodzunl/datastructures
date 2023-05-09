import time


def selectionsort(arr):
    n = len(arr)
    intercambios_totales = 0
    comparaciones_totales = 0

    for i in range(n):
        min_idx = i
        intercambios = 0
        comparaciones = 0

        for j in range(i + 1, n):
            comparaciones += 1
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            intercambios += 1
            intercambios_totales += 1
            print(f"Intercambio {arr[min_idx]} con {arr[i]}")
            print(f"Array actual: {arr}")
            time.sleep(1)

        comparaciones_totales += comparaciones
        print(f"Comparaciones realizadas en la iteración {i + 1}: {comparaciones}")
        print(f"Intercambios realizados en la iteración {i + 1}: {intercambios}\n")

    print(f"Comparaciones totales: {comparaciones_totales}")
    print(f"Intercambios totales: {intercambios_totales}")
