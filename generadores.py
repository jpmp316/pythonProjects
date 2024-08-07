import random
def generar_numeros():
    numeros = []
    n = int(input("Ingrese la cantidad de numero que quiere generar"))
    for i in range(n):
        numero=random.randint(1, 100)
        if numero%2==0:
            numeros.append(numero)

    yield numeros

num_par = generar_numeros()
# Calling the generator function and iterating over the returned iterator
for numero in num_par:
    print(numero)

print(type(num_par))