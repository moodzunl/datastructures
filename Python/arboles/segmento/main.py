import os
import time

class SegmentTree:
    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self.build(0, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.data[start]
        else:
            mid = (start + end) // 2
            self.build(2 * node + 1, start, mid)
            self.build(2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def imprimir(self, node=0, start=None, end=None, nivel=0):
        if start is None:
            start = 0
        if end is None:
            end = self.n - 1

        if start == end:
            print('  ' * nivel, self.tree[node])
        else:
            mid = (start + end) // 2
            self.imprimir(2 * node + 1, start, mid, nivel + 1)
            print('  ' * nivel, self.tree[node])
            self.imprimir(2 * node + 2, mid + 1, end, nivel + 1)


if __name__ == "__main__":
    data = [30, 40, 50, 35, 20, 25, 45, 15]
    segment_tree = SegmentTree(data)

    os.system('clear' if os.name == 'posix' else 'cls')
    print("Árbol de segmentos construido a partir del arreglo:", data)
    segment_tree.imprimir()