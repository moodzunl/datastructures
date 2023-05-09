import os
import time


class NodoB:
    def __init__(self, t):
        self.t = t
        self.hijos = [None] * (2 * t)
        self.claves = [None] * (2 * t - 1)
        self.n = 0
        self.hoja = True


class ArbolB:
    def __init__(self, t):
        self.t = t
        self.raiz = NodoB(t)

    def insertar(self, clave):
        r = self.raiz
        if r.n == 2 * self.t - 1:
            s = NodoB(self.t)
            self.raiz = s
            s.hoja = False
            s.hijos[0] = r
            self.dividir_hijo(s, 0)
            self.insertar_no_lleno(s, clave)
        else:
            self.insertar_no_lleno(r, clave)

    def insertar_no_lleno(self, x, k):
        i = x.n - 1
        if x.hoja:
            while i >= 0 and k < x.claves[i]:
                x.claves[i + 1] = x.claves[i]
                i -= 1
            x.claves[i + 1] = k
            x.n += 1
        else:
            while i >= 0 and k < x.claves[i]:
                i -= 1
            i += 1
            if x.hijos[i].n == 2 * self.t - 1:
                self.dividir_hijo(x, i)
                if k > x.claves[i]:
                    i += 1
            self.insertar_no_lleno(x.hijos[i], k)

    def dividir_hijo(self, x, i):
        t = self.t
        z = NodoB(t)
        y = x.hijos[i]
        z.hoja = y.hoja
        z.n = t - 1
        for j in range(t - 1):
            z.claves[j] = y.claves[j + t]
        if not y.hoja:
            for j in range(t):
                z.hijos[j] = y.hijos[j + t]
        y.n = t - 1
        for j in range(x.n, i, -1):
            x.hijos[j + 1] = x.hijos[j]
        x.hijos[i + 1] = z
        for j in range(x.n - 1, i - 1, -1):
            x.claves[j + 1] = x.claves[j]
        x.claves[i] = y.claves[t - 1]
        x.n += 1

    def imprimir(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz

        print("  " * nivel, end="")
        print(", ".join(str(k) for k in nodo.claves[: nodo.n]))

        if not nodo.hoja:
            for i in range(nodo.n + 1):
                self.imprimir(nodo.hijos[i], nivel + 1)
