import os
import time


class NodoAVL:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
        self.altura = 1


class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = NodoAVL(valor)
        else:
            self.raiz = self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if not nodo:
            return NodoAVL(valor)

        if valor < nodo.valor:
            nodo.izquierda = self._insertar(nodo.izquierda, valor)
        else:
            nodo.derecha = self._insertar(nodo.derecha, valor)

        nodo.altura = 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))

        balance = self._balance(nodo)

        if balance > 1:
            if valor < nodo.izquierda.valor:
                return self._rotar_derecha(nodo)
            else:
                nodo.izquierda = self._rotar_izquierda(nodo.izquierda)
                return self._rotar_derecha(nodo)

        if balance < -1:
            if valor > nodo.derecha.valor:
                return self._rotar_izquierda(nodo)
            else:
                nodo.derecha = self._rotar_derecha(nodo.derecha)
                return self._rotar_izquierda(nodo)

        return nodo

    def _altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def _balance(self, nodo):
        if not nodo:
            return 0
        return self._altura(nodo.izquierda) - self._altura(nodo.derecha)

    def _rotar_izquierda(self, z):
        y = z.derecha
        T2 = y.izquierda

        y.izquierda = z
        z.derecha = T2

        z.altura = 1 + max(self._altura(z.izquierda), self._altura(z.derecha))
        y.altura = 1 + max(self._altura(y.izquierda), self._altura(y.derecha))

        return y

    def _rotar_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha

        x.derecha = y
        y.izquierda = T2

        y.altura = 1 + max(self._altura(y.izquierda), self._altura(y.derecha))
        x.altura = 1 + max(self._altura(x.izquierda), self._altura(x.derecha))

        return x

    def imprimir(self, nodo=None, nivel=0):
        if not nodo:
            nodo = self.raiz
        if nodo.derecha:
            self.imprimir(nodo.derecha, nivel + 1)
        print("  " * nivel, nodo.valor)
        if nodo.izquierda:
            self.imprimir(nodo.izquierda, nivel + 1)


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def insertar_elementos_y_mostrar(arbol, array):
    for elemento in array:
        arbol.insertar(elemento)
        limpiar_pantalla()
        print(f"Insertando elemento: {elemento}\n")
        arbol.imprimir()
        time.sleep(1)
