from collections import deque


class Grafo:

    def __init__(self):

        self.grafo = {
            "Entrada": ["A"],
            "A": ["Entrada", "B", "C"],
            "B": ["A", "D"],
            "C": ["A"],
            "D": ["B"]
        }

    def ruta_mas_corta(self, inicio, destino):

        cola = deque([(inicio, [inicio])])

        visitados = set()

        while cola:

            nodo, camino = cola.popleft()

            if nodo == destino:
                return camino

            if nodo not in visitados:

                visitados.add(nodo)

                for vecino in self.grafo[nodo]:

                    cola.append((vecino, camino + [vecino]))

        return None