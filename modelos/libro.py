class Libro:
    def __init__(self, id, titulo, autor, categoria):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.disponible = True
        self.prestamos = 0

    def prestar(self):
        if self.disponible:
            self.disponible = False
            self.prestamos += 1
            return True
        return False

    def devolver(self):
        self.disponible = True

    def cambiar_disponibilidad(self):
        self.disponible = not self.disponible

    def mostrar(self):
        estado = "Disponible" if self.disponible else "Prestado"

        print(f"""
ID: {self.id}
Título: {self.titulo}
Autor: {self.autor}
Categoría: {self.categoria}
Estado: {estado}
Préstamos: {self.prestamos}
""")

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "autor": self.autor,
            "categoria": self.categoria,
            "disponible": self.disponible,
            "prestamos": self.prestamos
        }

    @classmethod
    def from_dict(cls, datos):
        libro = cls(
            datos["id"],
            datos["titulo"],
            datos["autor"],
            datos["categoria"]
        )
        libro.disponible = datos["disponible"]
        libro.prestamos = datos["prestamos"]
        return libro