import statistics
lista=[]
numeros = input("Ingrese numeros separados por comas")

# Dividir la cadena en elementos individuales y convertir cada uno a un entero
lista = [int(numero) for numero in numeros.split(',')]

suma = sum(lista)
promedio = sum(lista) / len(lista)

print(f"Suma: {suma}")
print(f"Promedio: {promedio}")
desviacion_estandar = statistics.stdev(lista)
print(f"Desviación estándar: {desviacion_estandar}")
print(lista)