def factorial(n):
    """Función que calcula el factorial de un número entero positivo.
    Parámetros
    n: Es un entero positivo.
    Devuelve el factorial de n.
    """
    tmp = 1
    for i in range(n):
        tmp *= i+1
    return tmp

def calcular_factura(precio,iva = 0.21):
    precio_total = precio+(precio*iva)

    return precio_total

factura = calcular_factura(200,0.8)
print(factura)

def areadelcirculo(radio):
    areac = 3.1416*(radio**2)
    return areac

resultado = areadelcirculo(78)
print(resultado)


def volumen_cilindro(h):
    resultado = areadelcirculo(80)
    vc = resultado*h

    return vc

volumen = volumen_cilindro(85)
print(volumen)