def crear_diccionario():
    diccionario = {}
    while True:
        clave = input("Ingrese una clave (o presione Enter para terminar): ")
        if clave == "":
            break
        valor = input(f"Ingrese el valor para '{clave}': ")
        diccionario[clave] = valor
    return diccionario

# Crear un diccionario con entradas del usuario
#mi_diccionario = crear_diccionario()
# Mostrar el diccionario resultante
#print("Diccionario creado:")
#for clave, valor in mi_diccionario.items():
   # print(f"{clave}: {valor}")


def crear_array():
    asignaturas = []
    posiciones = int(input("De cuantas posiciones quiere su arreglo?"))
    for i in range(posiciones):
        valores = input("Ingrese las asignaturas")
        asignaturas.append(valores)
        nota = int(input(f"Que nota sacaste en {asignaturas[i]}?"))
        print(f"Sacaste {nota} en la asignatura {asignaturas[i]}")
    return asignaturas



mi_arreglo = crear_array()
print("Arreglo creado exitosamente")
for valores in mi_arreglo:
    print(valores)


#arreglo= []

#for i in range(6):
    #valores = int(input("Introduce un numero ganador"))
    #arreglo.append(valores)
    #print("Los números ganadores son " + str(arreglo))