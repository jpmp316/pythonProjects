"""nombre_usuario = input("Escribe tu nombre")
numero = int(input("Digite un numero"))

print((nombre_usuario + "\n") * int(numero))
"""

while True:
    email = input("Ingrese su email: ")
    tiene_unarroba = email.count("@") == 1
    termina_con_arroba = email.endswith("@")
    arroba_principio = email.find("@") == 0

    if not tiene_unarroba or termina_con_arroba or arroba_principio:  
        print("Email incorrecto")
    else:
        print(email)
        break