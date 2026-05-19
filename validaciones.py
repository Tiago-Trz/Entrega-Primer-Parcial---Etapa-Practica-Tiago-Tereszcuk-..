def tiene_letra(cadena: str):
    """
    verifico si la cadena tiene al menos una letra (sea mayuscula o minuscula).
    recorrera la cadena manualmente comparando los valores ASCII.
    """
    encontre_letra = False
    indice = 0
    longitud = len(cadena)

    #itero mientras me queden caracteres y no haya encontrado una letra
    #evito el break controlando el ciclo de variables booleanas
    while indice < longitud and encontre_letra == False:
        caracter = cadena[indice]

        # comparo usando el orden alfabetico de la tabla ASCII
        if (caracter >= 'a' and caracter <= 'z') or (caracter >= 'A' and caracter <= 'Z'):
            encontre_letra = True

        indice += 1

    return encontre_letra

def ingresar_contrasenia():
    """
    solicito al usuario a ingresar una contraseña y valida que cumpla con los requisitos.
    me tendria que retornar que es valido.
    """
    contrasenia_valida = False
    contrasenia = ""

    while contrasenia_valida == False:
        contrasenia = input("Ingrese una contraseña nueva: ")
        longitud = len(contrasenia)

        #1. la contraseña no puede estar vacia
        if longitud == 0:
            print("Erorr: la contraseña no puede estar vacia.")
        #2. debe de tener 8 caracateres
        elif longitud < 8:
            print("Error: la contraseña debe contener al menos 8 caracteres.")
        #3. no puede comenzar con espacios
        elif contrsenia [0] == ' ':
            print("Error: la contraseña no puede comenzar con espacios.")
        #4. debe de tener al menos una letra
        elif tiene_letra(contrasenia) == False:
            print("Error: la contraseña debe contener al menos una letra.")
        else:
            #si cumple en cada prueba, cambia la bandera para salir del ciclo
            contrasenia_valida = True
            print("la contraseña ingresa esta correcta!")

return contrasenia

def tiene_numero(cadena: str):
    """
    verifico si la cadena tiene al menos un numero (del "0" al "9")
    """
    encontre_numero = False
    indice = 0 
    longitud = len(cadena)

    while indice < longitud and encontre_numero == False:
        caracter = cadena[indice]
        if caracter >= '0' and caracter <= '9':
            encontre_numero = True
        indice = indice + 1

    return encontre_numero

def tiene_simbolo(cadena: str):
    """
    verifico si la cadena tien alguno de los simbolos requeridos.
    utilizo la tabla ASCII desde el "!" hasta el "/".
    """
    encontre_simbolo = False
    indice = 0
    longitud = len(cadena)

    while indice < longitud and encontre_simbolo == False:
        caracter = cadena[indice]
        # en la tabla ASCII, los simbolos ! " # $ % & ' ( ) * + , - . / estab todos juntos
        if caracter >= '!' and caracter <= '/':
            encontre_simbolo = True
        indice = indice + 1

    return encontre_simbolo

def es_solo_letras(cadena: str):
    """
    verifico si la cadena contiene solo letras
    """
    solo_letras = True
    indice = 0 
    longitud = len(cadena)

    while indice < longitud and solo_letras == True:
        caracter = cadena[indice]
        es_minuscula = caracter >= 'a' and caracter <= 'z'
        es_mayuscula = caracter >= 'A' and caracter <= 'Z'

        #si el caracter NO es ni minuscula ni mayuscula, entonces no hay solamente letras
        if es_minuscula == False and es_mayuscula == False:
            solo_letras = False
        
        indice = indice + 1

    return solo_letras

def validar_seguridad(contrsenia: str):
    """
    determina el nivel de seguridad de la contraseña.
    """
    longitud = len(contrasenia)
    nivel = "No definido"

    #Fuerte: si contiene de todo y mas de 8 caracteres
    if longitud >= 12 and tiene_letra(contrasenia) and tiene_numero(contrasenia) and tiene_simbolo(contrasenia):
        nivel = "Fuerte"
    #Debil: entre 8 y 9, solo tiene letras
    elif (longitud == 8 or longitud == 9) and es_solo_letras(contrasenia):
        nivel = "Debil"
    #Media: tiene letras y numeros
    elif tiene_letra(contrsenia) and tiene_numero(contrsenia):
        nivel = "Media"
    else:
        nivel = "No cumplis con ninguno de los requisitos"

    return nivel