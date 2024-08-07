import re

while True:
    email = input("Ingrese su email: ").strip()  # Eliminar espacios en blanco al principio y al final
    tiene_unarroba = email.count("@") == 1
    termina_con_arroba = email.endswith("@")
    arroba_principio = email.startswith("@")
    dominio_valido = re.search(r"@\w+\.\w+", email) is not None

    if not tiene_unarroba or termina_con_arroba or arroba_principio or not dominio_valido:  
        print("Email incorrecto")
    else:
        print(email)
        break
