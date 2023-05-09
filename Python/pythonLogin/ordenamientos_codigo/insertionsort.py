import time


def insertionsort(arr):
    n = len(arr)
    intercambios_totales = 0
    comparaciones_totales = 0

    for i in range(1, n):
        clave = arr[i]
        j = i - 1
        comparaciones = 0
        intercambios = 0

        while j >= 0 and arr[j] > clave:
            comparaciones += 1
            arr[j + 1] = arr[j]
            j -= 1
            intercambios += 1
            intercambios_totales += 1
            print(f"Intercambio {arr[j + 1]} con {arr[j + 2]}")
            print(f"Array actual: {arr}")
            time.sleep(1)

        arr[j + 1] = clave
        comparaciones_totales += comparaciones

        print(f"Comparaciones realizadas en la iteración {i}: {comparaciones}")
        print(f"Intercambios realizados en la iteración {i}: {intercambios}\n")

    print(f"Comparaciones totales: {comparaciones_totales}")
    print(f"Intercambios totales: {intercambios_totales}")
