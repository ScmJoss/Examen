class Seccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []

    def conectar(self, otra_seccion):
        if otra_seccion not in self.conexiones:
            self.conexiones.append(otra_seccion)