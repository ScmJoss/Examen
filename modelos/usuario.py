class Usuario:
    LIMITE_LIBROS = 3

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.libros_prestados = []

    def puede_prestar(self):
        return len(self.libros_prestados) < self.LIMITE_LIBROS

    def prestar_libro(self, id_libro):
        if self.puede_prestar():
            self.libros_prestados.append(id_libro)
            return True
        return False

    def devolver_libro(self, id_libro):
        if id_libro in self.libros_prestados:
            self.libros_prestados.remove(id_libro)
            return True
        return False

    def mostrar(self):
        print(f"""
ID: {self.id}
Nombre: {self.nombre}
Libros prestados: {self.libros_prestados}
""")

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "libros_prestados": self.libros_prestados
        }

    @classmethod
    def from_dict(cls, datos):
        usuario = cls(datos["id"], datos["nombre"])
        usuario.libros_prestados = datos["libros_prestados"]
        return usuario