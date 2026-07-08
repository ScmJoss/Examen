import json
import os
from modelos.libro import Libro
from modelos.usuario import Usuario


# ================= LIBROS =================

def guardar_libros(libros):

    datos = []

    for libro in libros:
        datos.append(libro.to_dict())

    with open("datos/libros.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def cargar_libros():

    if not os.path.exists("datos/libros.json"):
        return []

    with open("datos/libros.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    return [Libro.from_dict(libro) for libro in datos]


# ================= USUARIOS =================

def guardar_usuarios(usuarios):

    datos = []

    for usuario in usuarios:
        datos.append(usuario.to_dict())

    with open("datos/usuarios.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)


def cargar_usuarios():

    if not os.path.exists("datos/usuarios.json"):
        return []

    with open("datos/usuarios.json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    return [Usuario.from_dict(usuario) for usuario in datos]


# ================= HISTORIAL =================

def guardar_historial(historial):

    with open("datos/prestamos.json", "w", encoding="utf-8") as archivo:
        json.dump(historial, archivo, indent=4, ensure_ascii=False)


def cargar_historial():

    if not os.path.exists("datos/prestamos.json"):
        return []

    with open("datos/prestamos.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)