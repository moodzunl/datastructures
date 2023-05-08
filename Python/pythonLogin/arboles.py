from tipos_arboles import (
    RedBlackTree,
    AVLTree,
    SegmentTree,
    BTree,
    DegenerateTree,
)

import math

arrays = []


def print_tree_red(node, level=0, indent="  "):
    if node is None or node.key is None:
        return

    print_tree_red(node.right, level + 1, indent)
    color = "R" if node.color == "red" else "B"
    print(f"{indent * level}{node.key}({color})")
    print_tree_red(node.left, level + 1, indent)


def print_tree_avl(node, level=0, indent="  "):
    if node is None:
        return

    print_tree_avl(node.right, level + 1, indent)
    print(f"{indent * level}{node.key}({node.height})")
    print_tree_avl(node.left, level + 1, indent)


def print_tree_seg(tree):
    n = len(tree) // 2
    height = int(math.ceil(math.log2(n))) + 1
    level = 0
    nodes_in_level = 1
    i = 1

    while level < height:
        print("Nivel", level, ": ", end="")
        for _ in range(nodes_in_level):
            if i < len(tree):
                print(tree[i], end=" ")
                i += 1
            else:
                break
        print()
        level += 1
        nodes_in_level *= 2

    print("Nivel hojas:", [tree[i] for i in range(n, len(tree))])


def print_btree(node, indent=""):
    if node is not None:
        if node.leaf:
            for i in range(node.n):
                print(indent, node.keys[i])
        else:
            for i in range(node.n):
                print_btree(node.children[i], indent + "  ")
                print(indent, node.keys[i])
            print_btree(node.children[node.n], indent + "  ")


def print_segment_tree(segment_tree, node=0, level=0, indent=4):
    if node < len(segment_tree.tree):
        left_child = 2 * node + 1
        right_child = 2 * node + 2

        print_segment_tree(segment_tree, left_child, level + 1, indent)
        print(" " * indent * level + f"{segment_tree.tree[node]}")
        print_segment_tree(segment_tree, right_child, level + 1, indent)


def print_degenerate_tree(node, indent=""):
    if node is not None:
        print_degenerate_tree(node.left, indent + "  ")
        print(indent, node.key)
        print_degenerate_tree(node.right, indent + "  ")


def arboles_rojonegro(array):
    rb_tree = RedBlackTree()
    for value in array:
        rb_tree.insert(value)

    print("Árbol Rojo-Negro generado:")
    print_tree_red(rb_tree.root)


def arboles_avl(array):
    avl_tree = AVLTree()
    # Insertar valores en el árbol
    for value in array:
        avl_tree.root = avl_tree.insert(avl_tree.root, value)

    print("Árbol AVL generado:")
    print_tree_avl(avl_tree.root)


def arboles_segmento(array):
    segment_tree = SegmentTree(
        array, function=min
    )  # Puedes cambiar la función según sea necesario
    print("Árbol de segmento generado:")
    print_segment_tree(segment_tree.tree)


def arboles_b(array, degree=3):
    b_tree = BTree(degree)
    for value in array:
        b_tree.insert(value)

    print("Árbol B generado:")
    print_btree(b_tree.root)


def arboles_degenerados(array):
    degenerate_tree = DegenerateTree()
    for value in array:
        degenerate_tree.insert(value)

    print("Árbol degenerado generado:")
    print_degenerate_tree(degenerate_tree.root)


def tipos_arboles(id_account):
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

            array_seleccionado = arrays[choiceOrder - 1].copy()

            print("Selecciona el tipo de arbol que deseas utilizar:")
            print("1. Arbol Rojo-Negro")
            print("2. Arbol AVL")
            print("3. Arbol de Segmento")
            print("4. Arbol B")
            print("5. Arbol Degenerado")

            seleccion = int(input())

            if seleccion == 1:
                arboles_rojonegro(array_seleccionado)
                input("Presiona enter para continuar. . .")
                input()
            elif seleccion == 2:
                arboles_avl(array_seleccionado)
                input("Presiona enter para continuar. . .")
                input()
            elif seleccion == 3:
                arboles_segmento(array_seleccionado)
                input("Presiona enter para continuar. . .")
                input()
            elif seleccion == 4:
                arboles_b(array_seleccionado)
                input("Presiona enter para continuar. . .")
                input()
            elif seleccion == 5:
                arboles_degenerados(array_seleccionado)
                input("Presiona enter para continuar. . .")
                input()
            else:
                print("Opción inválida.")
                return

    except FileNotFoundError:
        print("\n")
        print("El archivo no se encontró")
        input("Presiona enter para continuar. . .")
        input()
