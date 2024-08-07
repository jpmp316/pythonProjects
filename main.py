class Producto:
    def __init__(self, cod, nom, modelo, val, material):
        self.cod = cod
        self.nom = nom
        self.modelo = modelo
        self.val = val
        self.material = material

    def __str__(self):
        return (f"Código: {self.cod}, Nombre: {self.nom}, Modelo: {self.modelo}, "
                f"Valor: {self.val}, Material: {self.material}")


def ingresar_producto():
    while True:
        try:
            cod = int(input("Ingrese el código del producto: "))
            nom = input("Ingrese el nombre del producto: ")
            modelo = input("Ingrese el modelo del producto: ")
            val = int(input("Ingrese el valor del producto: "))
            material = input("Ingrese el material del producto: ")
            break
        except ValueError:
            print("Ingrese un valor válido")
    return Producto(cod, nom, modelo, val, material)

def mostrar_producto(producto):
    print("\nMostrando información del producto:")
    print(f"El código del producto es: {producto.cod}")
    print(f"El nombre del producto es: {producto.nom}")
    print(f"El modelo del producto es: {producto.modelo}")
    print(f"El valor del producto es: {producto.val}")
    print(f"El material del producto es: {producto.material}")

def eliminar_producto(productos, indice):
    del productos[indice]

def listar_productos(productos):
    print("\nLista de productos:")
    for producto in productos:
        print(producto)

def main():
    n = int(input("Ingrese el número de productos: "))
    productos = []

    for i in range(n):
        print(f"\nProducto {i+1}:")
        producto = ingresar_producto()
        productos.append(producto)

    while True:
        print("\nMenú")
        print("1. Mostrar información de un producto")
        print("2. Modificar información de un producto")
        print("3. Eliminar un producto")
        print("4. Listar todos los productos")
        print("5. Salir")
        op = int(input("Seleccione una opción: "))

        if op == 1:
            index = int(input("Ingrese el índice del producto a mostrar (0 a n-1): "))
            if 0 <= index < len(productos):
                mostrar_producto(productos[index])
            else:
                print("Índice inválido")
        elif op == 2:
            index = int(input("Ingrese el índice del producto a modificar (0 a n-1): "))
            if 0 <= index < len(productos):
                print("\nModificar información")
                productos[index] = ingresar_producto()
                conf = input("Digite 'si' para confirmar los cambios: ")
                if conf == "si":
                    mostrar_producto(productos[index])
            else:
                print("Índice inválido")
        elif op == 3:
            while True:
                try:
                    index = int(input("Ingrese el índice del producto a eliminar (0 a n-1): "))
                    break
                except ValueError:
                    print("Ingrese un numero entero")
            if 0 <= index < len(productos):
                eliminar_producto(productos, index)
                print("Producto eliminado.")
            else:
                print("Índice inválido")
        elif op == 4:
            listar_productos(productos)
        elif op == 5:
            break  # Salir del bucle
        else:
            print("Ingresó una opción errónea")

    print("\nLista final de productos:")
    listar_productos(productos)

if __name__ == "__main__":
    main()
