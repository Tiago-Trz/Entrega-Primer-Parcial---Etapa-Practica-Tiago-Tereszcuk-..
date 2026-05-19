import utilidades

def contar_tipos_caracteres(contrasenia: str):
    """
    cuenta y me muestra por pantalla todos los caracteres escritos.
    esto recorre manualmente la cadena de texto
    """
    letras = 0
    numeros = 0
    simbolos = 0
    espacios = 0
    
    longitud = len(contrasenia)
    
    # recorro cada posicion de la contraseña
    for indice in range(longitud):
        caracter = contrasenia[indice]
        
        #si es letra
        if (caracter >= 'a' and caracter <= 'z') or (caracter >= 'A' and caracter <= 'Z'):
            letras = letras + 1
        #si es número
        elif caracter >= '0' and caracter <= '9':
            numeros = numeros + 1
        #si es espacio
        elif caracter == ' ':
            espacios = espacios + 1
        #si es un símbolo permitido (! hasta /)
        elif caracter >= '!' and caracter <= '/':
            simbolos = simbolos + 1
            
    print("\n--- Conteo de Caracteres ---")
    print(f"Cantidad de letras: {letras}")
    print(f"Cantidad de números: {numeros}")
    print(f"Cantidad de símbolos: {simbolos}")
    print(f"Cantidad de espacios: {espacios}")


def buscar_caracter(contrasenia: str):
    """
    solicito un carácter al usuario, me tiene que decir cuantas veces aparece y guarda la posicion.
    """
    caracter_buscado = input("Ingrese el único carácter que desea buscar: ")
    cantidad = 0
    posiciones = "" 

    longitud = len(contrasenia)
    
    for indice in range(longitud):
        if contrasenia[indice] == caracter_buscado:
            cantidad = cantidad + 1
            posiciones = posiciones + str(indice) + " "
            
    print("\n--- Resultado de la Búsqueda ---")
    if cantidad > 0:
        print(f"El carácter '{caracter_buscado}' aparece {cantidad} veces.")
        print(f"Posiciones exactas en las que aparece: {posiciones}")
    else:
        print(f"El carácter '{caracter_buscado}' no se encontró en la contraseña.")

def verificar_palindromo(contrasenia: str):
    """
    verifica si la contraseña es un palíndromo comparándola con su versión invertida.
    """
    # reutilizo la función del módulo utilidades
    contrasenia_invertida = utilidades.invertir_cadena(contrasenia)
    
    print("\n--- Verificación de Palíndromo ---")
    if contrasenia == contrasenia_invertida:
        print("La contraseña ES un palíndromo (se lee igual al derecho y al revés).")
    else:
        print("La contraseña NO es un palíndromo.")
