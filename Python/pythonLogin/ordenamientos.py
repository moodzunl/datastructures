from ordenamientos_codigo.bubblesort import bubblesort
from ordenamientos_codigo.insertionsort import insertionsort
from ordenamientos_codigo.mergesort import mergesort
from ordenamientos_codigo.quicksort import quicksort
from ordenamientos_codigo.selectionsort import selectionsort

arrays = []


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
                print(f"Array inicial: {array_seleccionado}\n")
                print("-----------------Inicio de QuickSort-----------------")
                quicksort(array_seleccionado, 0, len(array_seleccionado) - 1)
                print("-----------------Fin de QuickSort-----------------")
                print(f"Array ordenado: {array_seleccionado}")
                input("Presiona enter para continuar. . .")
            elif ordenamiento == 2:
                print(f"Array inicial: {array_seleccionado}\n")
                print("-----------------Inicio de BubbleSort-----------------")
                bubblesort(array)
                print("-----------------Fin de BubbleSort-----------------")
                print(f"Array ordenado: {array_seleccionado}")
                input("Presiona enter para continuar. . .")
            elif ordenamiento == 3:
                print(f"Array inicial: {array_seleccionado}\n")
                print("-----------------Inicio de InsertSort-----------------")
                insertionsort(array_seleccionado)
                print("-----------------Fin de InsertSort-----------------")
                print(f"Array ordenado: {array_seleccionado}")
                input("Presiona enter para continuar. . .")
            elif ordenamiento == 4:
                print(f"Array inicial: {array_seleccionado}\n")
                print("-----------------Inicio de MergeSort-----------------")
                mergesort(array_seleccionado)
                print("-----------------Fin de MergeSort-----------------")
                print(f"Array ordenado: {array_seleccionado}")
                input("Presiona enter para continuar. . .")
            elif ordenamiento == 5:
                print(f"Array inicial: {array_seleccionado}\n")
                print("-----------------Inicio de SelectionSort-----------------")
                selectionsort(array_seleccionado)
                print("-----------------Fin de SelectionSort-----------------")
                print(f"Array ordenado: {array_seleccionado}")
                input("Presiona enter para continuar. . .")
            else:
                print("Opción inválida.")
                return

    except FileNotFoundError:
        print("\n")
        print("El archivo no se encontró")
        input("Presiona enter para continuar. . .")
        input()
