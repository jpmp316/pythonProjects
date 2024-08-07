class Curso:
    def __init__(self,nombre,creditos,codigo):
        self.nombre = nombre
        self.creditos = creditos
        self.codigo = codigo
        self.estudiantes = []

    def inscribir_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def eliminar_estudiante(self, estudiante):
        self.estudiantes.remove(estudiante)

    def listar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante)

    def __str__(self):
        est_str = ", ".join(str(estudiante) for estudiante in self.estudiantes)
        return f"Nombre: {self.nombre},Creditos: {self.creditos},Codigo:{self.codigo} Lista de estudiantes: [{est_str}]"


class Estudiante:
    def __init__(self,nombre,matricula):
        self.nombre = nombre
        self.matricula = matricula

    def __str__(self):
        return f"Nombre : {self.nombre},Matricula{self.matricula}"


class Instituto:
    def __init__(self):
        self.cursos = []
        self.estudiantes = []

    def agregar_curso(self,curso):
        self.cursos.append(curso)

    def registrar_estudiante(self,estudiante):
        self.estudiantes.append(estudiante)

    def inscribir_estudiante_en_curso(self,matricula_estudiante,codigo_curso):
        estudiante = None
        for e in instituto.estudiantes:
            if e.matricula == matricula_estudiante:
                estudiante = e
                break
        if estudiante is not None:
            for curso in instituto.cursos:
                if curso.codigo == codigo_curso:
                    curso.inscribir_estudiante(estudiante)
                    print("Estudiante añadido")
        else:
            print("Estudiante no encontrado")

    def listar_cursos(self):
        for curso in instituto.cursos:
            print(curso)

    def listar_estudiantes(self):
        for estudiante in instituto.estudiantes:
            print(estudiante)


Matematicas = Curso("Matematicas",3,5)
Juan = Estudiante("Juan",45)
Nata = Estudiante("Nata",1)
instituto = Instituto()
instituto.agregar_curso(Matematicas)
instituto.registrar_estudiante(Juan)
instituto.registrar_estudiante(Nata)
instituto.inscribir_estudiante_en_curso(45,5)
instituto.inscribir_estudiante_en_curso(1,5)
instituto.listar_cursos()
instituto.listar_estudiantes()
Matematicas.listar_estudiantes()
