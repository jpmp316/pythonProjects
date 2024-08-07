def sumar_elementos(lista):
    suma = 0
    for i in lista:
        suma += i

    return suma


lista = [1, 3, 4, 45]
resultado = sumar_elementos(lista)
print(resultado)

"""
Escribe una función promedio_notas(estudiantes) que reciba un diccionario donde las claves son nombres de estudiantes y los valores son listas de notas. La función debe devolver un nuevo diccionario con los promedios de cada estudiante.
1 paso: crear el diccionario y darle nombres de clave y de valor sus notas
2 paso: crear la funcion que reciba como parametro el diccionario
3 paso: 
"""
estudiantes = {}
while True:
    clave = input("Ingrese el nombre del estudiante o pulse enter para salir ")
    if clave == "":
        break
    notas = []
    nro_notas = int(input("Cuantas notas va a ingresar?"))
    for i in range(nro_notas):
        nota = int(input("Ingrese la calificacion"))
        notas.append(nota)

    estudiantes[clave] = {"Notas": notas}
for clave,valor in estudiantes.items():
    print(f"Nombre:{clave}")
    print(f"Notas{notas}")

def promedio_estudiantes(estudiantes):
    promedios = {}
    for clave, datos in estudiantes.items():
        notas = datos["Notas"]
        if notas:  # Verificar que la lista de notas no esté vacía
            promedio = sum(notas) / len(notas)
        else:
            promedio = 0
        promedios[clave] = promedio
    return promedios

promedios = promedio_estudiantes(estudiantes)
for estudiante, promedio in promedios.items():
    print(f"El promedio de notas para {estudiante} es: {promedio:.2f}")