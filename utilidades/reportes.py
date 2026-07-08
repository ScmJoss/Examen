def ordenar_por_titulo(libros):
    return sorted(libros, key=lambda libro: libro.titulo.lower())


def ordenar_por_autor(libros):
    return sorted(libros, key=lambda libro: libro.autor.lower())


def ordenar_por_prestamos(libros):
    return sorted(libros, key=lambda libro: libro.prestamos, reverse=True)


def libro_mas_prestado(libros):

    if len(libros) == 0:
        return None

    return max(libros, key=lambda libro: libro.prestamos)


def usuario_con_mas_prestamos(usuarios):

    if len(usuarios) == 0:
        return None

    return max(usuarios, key=lambda usuario: len(usuario.libros_prestados))