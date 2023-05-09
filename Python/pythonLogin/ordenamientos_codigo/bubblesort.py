import time


def bubblesort(arr):
    n = len(arr)
    intercambios_totales = 0
    comparaciones_totales = 0

    for i in range(n):
        intercambios = 0
        for j in range(0, n - i - 1):
            comparaciones_totales += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambios += 1
                intercambios_totales += 1
                print(f"Intercambio {arr[j]} con {arr[j + 1]}")
                print(f"Array actual: {arr}")
                time.sleep(1)

        print(f"Comparaciones realizadas en la iteración {i + 1}: {n - i - 1}")
        print(f"Intercambios realizados en la iteración {i + 1}: {intercambios}\n")
        print("----------------------------------------")

    print(f"Comparaciones totales: {comparaciones_totales}")
    print(f"Intercambios totales: {intercambios_totales}")
