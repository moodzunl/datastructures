import os
import time
import enum


class Color(enum.Enum):
    ROJO = 1
    NEGRO = 2


class NodoRN:
    def __init__(
        self, valor, color=Color.ROJO, padre=None, izquierda=None, derecha=None
    ):
        self.valor = valor
        self.color = color
        self.padre = padre
        self.izquierda = izquierda
        self.derecha = derecha


class ArbolRN:
    def __init__(self):
        self.nil = NodoRN(None, Color.NEGRO)
        self.raiz = self.nil

    def insertar(self, valor):
        nodo = NodoRN(valor, padre=self.nil, izquierda=self.nil, derecha=self.nil)
        self._insertar_nodo(nodo)
        self._arreglar_insercion(nodo)

    def _insertar_nodo(self, z):
        y = self.nil
        x = self.raiz

        while x != self.nil:
            y = x
            if z.valor < x.valor:
                x = x.izquierda
            else:
                x = x.derecha

        z.padre = y

        if y == self.nil:
            self.raiz = z
        elif z.valor < y.valor:
            y.izquierda = z
        else:
            y.derecha = z

    def _arreglar_insercion(self, z):
        while z.padre.color == Color.ROJO:
            if z.padre == z.padre.padre.izquierda:
                y = z.padre.padre.derecha
                if y.color == Color.ROJO:
                    z.padre.color = Color.NEGRO
                    y.color = Color.NEGRO
                    z.padre.padre.color = Color.ROJO
                    z = z.padre.padre
                else:
                    if z == z.padre.derecha:
                        z = z.padre
                        self.rotar_izquierda(z)
                    z.padre.color = Color.NEGRO
                    z.padre.padre.color = Color.ROJO
                    self.rotar_derecha(z.padre.padre)
            else:
                y = z.padre.padre.izquierda
                if y.color == Color.ROJO:
                    z.padre.color = Color.NEGRO
                    y.color = Color.NEGRO
                    z.padre.padre.color = Color.ROJO
                    z = z.padre.padre
                else:
                    if z == z.padre.izquierda:
                        z = z.padre
                        self.rotar_derecha(z)
                    z.padre.color = Color.NEGRO
                    z.padre.padre.color = Color.ROJO
                    self.rotar_izquierda(z.padre.padre)

        self.raiz.color = Color.NEGRO

    def rotar_izquierda(self, x):
        y = x.derecha
        x.derecha = y.izquierda

        if y.izquierda != self.nil:
            y.izquierda.padre = x

        y.padre = x.padre

        if x.padre == self.nil:
            self.raiz = y
        elif x == x.padre.izquierda:
            x.padre.izquierda = y
        else:
            x.padre.derecha = y

        y.izquierda = x
        x.padre = y

    def rotar_derecha(self, x):
        y = x.izquierda
        x.izquierda = y.derecha

        if y.derecha != self.nil:
            y.derecha.padre = x

        y.padre = x.padre

        if x.padre == self.nil:
            self.raiz = y
        elif x == x.padre.derecha:
            x.padre.derecha = y
        else:
            x.padre.izquierda = y

        y.derecha = x
        x.padre = y

    def imprimir(self, nodo=None, nivel=0):
        if not self.raiz:
            print("Árbol vacío")
            return

        if not nodo:
            nodo = self.raiz

        if nodo.derecha != self.nil:
            self.imprimir(nodo.derecha, nivel + 1)
        print("  " * nivel, nodo.valor, nodo.color)
        if nodo.izquierda != self.nil:
            self.imprimir(nodo.izquierda, nivel + 1)
