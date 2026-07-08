from modelos.libro import Libro
from modelos.usuario import Usuario
from datetime import datetime


class Biblioteca:

    def __init__(self):
        self.libros = []
        self.usuarios = []
        self.historial = []

    # ================= LIBROS =================

    def agregar_libro(self, id, titulo, autor, categoria):
        for libro in self.libros:
            if libro.id == id:
                print("Ese ID ya existe.")
                return

        self.libros.append(Libro(id, titulo, autor, categoria))
        print("Libro agregado correctamente.")

    def mostrar_libros(self):

        if len(self.libros) == 0:
            print("No hay libros registrados.")
            return

        print("\n===== CATÁLOGO =====")

        for libro in self.libros:
            libro.mostrar()

    def buscar_libro(self, titulo):

        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                libro.mostrar()
                return libro

        print("Libro no encontrado.")
        return None

    def cambiar_disponibilidad(self, id):

        for libro in self.libros:
            if libro.id == id:
                libro.cambiar_disponibilidad()
                print("Disponibilidad actualizada.")
                return

        print("Libro no encontrado.")

    # ================= USUARIOS =================

    def registrar_usuario(self, id, nombre):

        for usuario in self.usuarios:
            if usuario.id == id:
                print("Ese usuario ya existe.")
                return

        self.usuarios.append(Usuario(id, nombre))
        print("Usuario registrado.")

    def mostrar_usuarios(self):

        if len(self.usuarios) == 0:
            print("No hay usuarios.")

        for usuario in self.usuarios:
            usuario.mostrar()

    # ================= PRÉSTAMOS =================

    def prestar_libro(self, id_usuario, id_libro):

        usuario = None
        libro = None

        for u in self.usuarios:
            if u.id == id_usuario:
                usuario = u
                break

        for l in self.libros:
            if l.id == id_libro:
                libro = l
                break

        if usuario is None:
            print("Usuario inexistente.")
            return

        if libro is None:
            print("Libro inexistente.")
            return

        if not usuario.puede_prestar():
            print("El usuario ya tiene 3 libros.")
            return

        if not libro.disponible:
            print("El libro no está disponible.")
            return

        usuario.prestar_libro(libro.id)
        libro.prestar()

        fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

        self.historial.append({
            "usuario": usuario.nombre,
            "libro": libro.titulo,
            "fecha": fecha
        })

        print("Préstamo realizado correctamente.")

    # ================= DEVOLUCIONES =================

    def devolver_libro(self, id_usuario, id_libro):

        usuario = None
        libro = None

        for u in self.usuarios:
            if u.id == id_usuario:
                usuario = u

        for l in self.libros:
            if l.id == id_libro:
                libro = l

        if usuario is None or libro is None:
            print("Datos incorrectos.")
            return

        if usuario.devolver_libro(id_libro):

            libro.devolver()

            print("Libro devuelto correctamente.")

        else:

            print("Ese usuario no tenía ese libro.")

    # ================= HISTORIAL =================

    def mostrar_historial(self):

        if len(self.historial) == 0:

            print("No existen préstamos.")

            return

        print("\n===== HISTORIAL =====")

        for registro in self.historial:

            print(f"""
Usuario : {registro['usuario']}
Libro   : {registro['libro']}
Fecha   : {registro['fecha']}
------------------------------
""")