import os
import time
from estructura_arboles.arbol_avl import ArbolAVL
from estructura_arboles.arbol_b import ArbolB
from estructura_arboles.arbol_degenerado import ArbolDegenerado
from estructura_arboles.arbol_rojo_negro import ArbolRN
from estructura_arboles.arbol_segmento import SegmentTree


arrays = []


def tipos_arboles(id_account):
    arrays.clear()

    try:
        with open("lista.txt", "r") as file:
            for line in file:
                fields = line.strip().split(":")
                if fields[1] == id_account:
                    arrays.append(list(map(int, fields[0].split(","))))
            for i, array in enumerate(arrays):
                print(f"{i+1}. {array}")

            print("Selecciona el arreglo que deseas ordenar")
            choiceOrder = int(input())

            if choiceOrder < 1 or choiceOrder > len(arrays):
                print("La opción seleccionada no es válida")
                return

            array_seleccionado = arrays[choiceOrder - 1].copy()

            print("Selecciona el tipo de arbol que deseas utilizar:")
            print("1. Arbol Rojo-Negro")
            print("2. Arbol AVL")
            print("3. Arbol de Segmento")
            print("4. Arbol B")
            print("5. Arbol Degenerado")

            seleccion = int(input())

            if seleccion == 1:
                arbol = ArbolRN()
                for valor in array_seleccionado:
                    os.system("clear" if os.name == "posix" else "cls")
                    print(f"Insertando {valor}")
                    arbol.insertar(valor)
                    arbol.imprimir()
                    time.sleep(1)
                input("Presiona enter para continuar. . .")
            elif seleccion == 2:
                arbol = ArbolAVL()
                for valor in array_seleccionado:
                    arbol.insertar(valor)
                    os.system("clear" if os.name == "posix" else "cls")
                    print(f"Insertando elemento: {valor}\n")
                    arbol.imprimir()
                    time.sleep(1)
                input("Presiona enter para continuar. . .")
            elif seleccion == 3:
                segment_tree = SegmentTree(array_seleccionado)
                os.system("clear" if os.name == "posix" else "cls")
                print(
                    "Árbol de segmentos construido a partir del arreglo:",
                    array_seleccionado,
                )
                segment_tree.imprimir()
                input("Presiona enter para continuar. . .")
            elif seleccion == 4:
                t = 2
                arbol_b = ArbolB(t)
                for valor in array_seleccionado:
                    os.system("clear" if os.name == "posix" else "cls")
                    print(f"Insertando {valor}")
                    arbol_b.insertar(valor)
                    arbol_b.imprimir()
                    time.sleep(1)
                input("Presiona enter para continuar. . .")
            elif seleccion == 5:
                arbol_degenerado = ArbolDegenerado()
                for valor in array_seleccionado:
                    os.system("clear" if os.name == "posix" else "cls")
                    print(f"Insertando {valor}")
                    arbol_degenerado.insertar(valor)
                    arbol_degenerado.imprimir()
                    time.sleep(1)
                input("Presiona enter para continuar. . .")
            else:
                print("Opción inválida.")
                return

    except FileNotFoundError:
        print("\n")
        print("El archivo no se encontró")
        input("Presiona enter para continuar. . .")
        input()
