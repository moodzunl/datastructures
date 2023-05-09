import os
import time


class NodoDegenerado:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


class ArbolDegenerado:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoDegenerado(valor)
        else:
            nodo_actual = self.raiz
            while True:
                if valor < nodo_actual.valor:
                    if nodo_actual.izquierda is None:
                        nodo_actual.izquierda = NodoDegenerado(valor)
                        break
                    else:
                        nodo_actual = nodo_actual.izquierda
                else:
                    if nodo_actual.derecha is None:
                        nodo_actual.derecha = NodoDegenerado(valor)
                        break
                    else:
                        nodo_actual = nodo_actual.derecha

    def imprimir(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz

        if nodo.derecha is not None:
            self.imprimir(nodo.derecha, nivel + 1)
        print("  " * nivel, nodo.valor)
        if nodo.izquierda is not None:
            self.imprimir(nodo.izquierda, nivel + 1)
