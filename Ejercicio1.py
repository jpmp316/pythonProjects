def depositar_dinero():
    while True:
        try:
            deposito = float(input("Ingrese el depósito: "))
            if deposito > 0:
                return deposito
            else:
                print("Por favor, ingrese un valor positivo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def ingresar_inicial():
    while True:
        try:
            inicial = float(input("Ingrese el dinero inicial: "))
            if inicial >= 0:
                return inicial
            else:
                print("Por favor, ingrese un valor no negativo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def ver_saldo(saldo):
    print(f"El saldo actual es: ${saldo:.2f}")

def retirar_dinero():
    while True:
        try:
            retiro = float(input("Ingrese la cantidad a retirar: "))
            if retiro > 0:
                return retiro
            else:
                print("Por favor, ingrese un valor positivo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")




def main():
    saldo = ingresar_inicial()
    opcion = 0
    contador = 0
    while opcion != 4:
        contador+=1
        print("MENÚ")
        print("1.Depositar dinero")
        print("2.Retirar dinero")
        print("3.Ver saldo actual")
        print("4.Salir")
        try:
            opcion = int(input("Que desea hacer?"))
            if opcion == 1:
                deposito = depositar_dinero()
                saldo = saldo+deposito
            elif opcion == 2:
                retiro = retirar_dinero()
                if retiro <= saldo:
                    saldo -= retiro
                else:
                    print("Saldo insuficiente")
            elif opcion == 3:
                ver_saldo(saldo)
            elif opcion ==4:
                print(f"Programa terminado con {contador} Operaciones")
                print(f"Saldo final: ${saldo:.2f}")
                break
            else:
                print("Opción no válida. Por favor, elija una opción entre 1 y 4.")
        except ValueError:
            print("Por favor, ingrese un número válido.")









if __name__ == "__main__":
        main()