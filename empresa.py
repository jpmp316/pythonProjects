# Definir la clase Empleado
class Empleado:
    def __init__(self, nombre, edad, cargo, salario):
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
        self.salario = salario

    def calcular_incremento(self, porcentaje):
        self.salario *= (1 + porcentaje / 100)

    def __str__(self):
        return f"{self.nombre}, {self.edad} años, {self.cargo}, salario: ${self.salario:.2f}"

# Definir la clase Empresa
class Empresa:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def buscar_empleado(self, nombre):
        for empleado in self.empleados:
            if empleado.nombre == nombre:
                return empleado
        return None

    def listar_empleados(self):
        for empleado in self.empleados:
            print(empleado)

# Ejemplo de uso
empresa = Empresa()

empleado1 = Empleado("Juan Pérez", 30, "Desarrollador", 50000.0)
empleado2 = Empleado("María López", 25, "Diseñador", 45000.0)

empresa.agregar_empleado(empleado1)
empresa.agregar_empleado(empleado2)

print("Lista de empleados:")
empresa.listar_empleados()

print("\nIncremento salarial del 5% para Juan Pérez:")
juan = empresa.buscar_empleado("Juan Pérez")
if juan:
    juan.calcular_incremento(5)
    print(juan)
else:
    print("Empleado no encontrado.")
