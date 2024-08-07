class Persona:
    def __init__(self,nombre,residencia,edad):
        self.nombre = nombre
        self.residencia = residencia
        self.edad = edad

    def descripcion(self):
        print(f"Nombre: {self.nombre}, Residencia: {self.residencia}, Edad: {self.edad}")
    


    
class Empleado(Persona):
    def __init__(self,salario,antiguedad,nombre,residencia,edad):
        super().__init__(nombre,edad,residencia)
        self.salario = salario
        self.antiguedad = antiguedad
        

    def descripcion(self):
        super().descripcion()
        print(f"Salario: {self.salario} Antiguedad: {self.antiguedad}")

        
Juan = Empleado(23,2,"Juan","Sincelejo","23")
Juan.descripcion()
print(isinstance(Juan,Empleado))