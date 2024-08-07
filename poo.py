class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.aniopublicacion = anio_publicacion
        self.disponible = True


    def prestar(self):
        self.disponible = False
        print("el libro ha sido prestado")

    def devolver(self):
        self.disponible = True
        print("El libro ha sido devuelto")

    def __str__(self):
        return (f"Titulo: {self.titulo}, Autor: {self.autor}, Año: {self.aniopublicacion}, "
                f"disponible: {self.disponible}")


class Miembro:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def prestar_libro(self,libro):
        self.libros_prestados.append(libro)
        print("El libro ha sido prestado al miembro")

    def devolver_libro(self,libro):
        self.libros_prestados.remove(libro)

    def __str__(self):
        libros_str = ", ".join(str(libro) for libro in self.libros_prestados)
        return f"Nombre: {self.nombre}, Libros prestados: [{libros_str}]"

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.miembros = []

    def agregar_libro(self,libro):
        self.libros.append(libro)

    def registrar_miembro(self,miembro):
        self.miembros.append(miembro)

    def prestar_libro_a_miembro(self, titulo_libro, nombre_miembro):
        miembro = None
        for m in biblioteca.miembros:
            if m.nombre == nombre_miembro:
                miembro = m
                break

        # Verifica si el miembro fue encontrado
        if miembro is not None:
            # Encuentra el libro y actualiza su estado
            for libro in biblioteca.libros:
                if libro.titulo == titulo_libro:
                    if libro.disponible:  # Verifica si el libro está disponible
                        libro.prestar()
                        miembro.prestar_libro(libro)
                        break
        else:
            print("Miembro no encontrado")

    def devolver_libro(self,titulo_libro,nombre_miembro):
        miembro = None
        for m in biblioteca.miembros:
            if m.nombre == nombre_miembro:
                miembro = m
                break

        # Verifica si el miembro fue encontrado
        if miembro is not None:
            # Encuentra el libro y actualiza su estado
            for libro in biblioteca.libros:
                if libro.titulo == titulo_libro:
                    if libro.disponible == False:  # Verifica si el libro está disponible
                        miembro.devolver_libro(libro)
                        libro.devolver()
                        break
        else:
            print("Miembro no encontrado")

    def __str__(self):
        libros_str = ", ".join(str(libro) for libro in self.libros)
        miembros_str = ", ".join(str (miembro) for miembro in self.miembros)
        return f" Libros: [{libros_str}], Miembros: [{miembros_str}]"


libro1 = Libro("El Quijote", "Miguel de Cervantes", 1605)
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
libro3 = Libro("1984", "George Orwell", 1949)
miembro1 = Miembro("Juan Pérez")
miembro2 = Miembro("María López")
biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
# Registrar miembros en la biblioteca
biblioteca.registrar_miembro(miembro1)
biblioteca.registrar_miembro(miembro2)
biblioteca.prestar_libro_a_miembro("El Quijote", "Juan Pérez")
cadena_miembro = miembro1.__str__()
print(cadena_miembro)
biblioteca.devolver_libro("El Quijote", "Juan Pérez")
cadena_miembro = miembro1.__str__()
print(cadena_miembro)
library = biblioteca.__str__()
print(library)