from biblioteca import Biblioteca
from utilidades.archivos import (
    guardar_libros,
    guardar_usuarios,
    guardar_historial,
    cargar_libros,
    cargar_usuarios,
    cargar_historial
)

from utilidades.reportes import (
    ordenar_por_titulo,
    ordenar_por_autor,
    ordenar_por_prestamos,
    libro_mas_prestado,
    usuario_con_mas_prestamos
)

from utilidades.grafo import Grafo


biblioteca = Biblioteca()

# Cargar datos al iniciar
biblioteca.libros = cargar_libros()
biblioteca.usuarios = cargar_usuarios()
biblioteca.historial = cargar_historial()

grafo = Grafo()

while True:

    print("""
=============================
 SISTEMA DE BIBLIOTECA
=============================

1. Agregar libro
2. Mostrar catálogo
3. Buscar libro
4. Cambiar disponibilidad
5. Registrar usuario
6. Mostrar usuarios
7. Prestar libro
8. Devolver libro
9. Historial
10. Reportes
11. Ruta más corta
0. Guardar y salir
""")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        id = input("ID: ")
        titulo = input("Título: ")
        autor = input("Autor: ")
        categoria = input("Categoría: ")

        biblioteca.agregar_libro(id, titulo, autor, categoria)

    elif opcion == "2":

        biblioteca.mostrar_libros()

    elif opcion == "3":

        titulo = input("Título del libro: ")
        biblioteca.buscar_libro(titulo)

    elif opcion == "4":

        id = input("ID del libro: ")
        biblioteca.cambiar_disponibilidad(id)

    elif opcion == "5":

        id = input("ID del usuario: ")
        nombre = input("Nombre: ")

        biblioteca.registrar_usuario(id, nombre)

    elif opcion == "6":

        biblioteca.mostrar_usuarios()

    elif opcion == "7":

        usuario = input("ID Usuario: ")
        libro = input("ID Libro: ")

        biblioteca.prestar_libro(usuario, libro)

    elif opcion == "8":

        usuario = input("ID Usuario: ")
        libro = input("ID Libro: ")

        biblioteca.devolver_libro(usuario, libro)

    elif opcion == "9":

        biblioteca.mostrar_historial()

    elif opcion == "10":

        print("""
========= REPORTES =========
1. Ordenar por título
2. Ordenar por autor
3. Ordenar por préstamos
4. Libro más prestado
5. Usuario con más préstamos
""")

        op = input("Seleccione: ")

        if op == "1":

            for libro in ordenar_por_titulo(biblioteca.libros):
                libro.mostrar()

        elif op == "2":

            for libro in ordenar_por_autor(biblioteca.libros):
                libro.mostrar()

        elif op == "3":

            for libro in ordenar_por_prestamos(biblioteca.libros):
                libro.mostrar()

        elif op == "4":

            libro = libro_mas_prestado(biblioteca.libros)

            if libro:
                print("\nLibro más prestado:\n")
                libro.mostrar()

        elif op == "5":

            usuario = usuario_con_mas_prestamos(biblioteca.usuarios)

            if usuario:
                usuario.mostrar()

    elif opcion == "11":

        inicio = input("Nodo inicial: ")
        destino = input("Nodo destino: ")

        ruta = grafo.ruta_mas_corta(inicio, destino)

        if ruta:
            print("\nRuta encontrada:")
            print(" -> ".join(ruta))
        else:
            print("No existe ruta.")

    elif opcion == "0":

        guardar_libros(biblioteca.libros)
        guardar_usuarios(biblioteca.usuarios)
        guardar_historial(biblioteca.historial)

        print("Datos guardados correctamente.")
        print("Hasta luego.")

        break

    else:

        print("Opción inválida.")