def invertir_cadena(cadena: str):
    """
    recibe una cadena y la trae invertida recorriendola desde atras hacias delante.
    """
    cadena_invertida = ""
    longitud = len(cadena)
    
    # recorro la cadena
    for indice in range(longitud - 1, -1, -1):
        caracter = cadena[indice]
        cadena_invertida = cadena_invertida + caracter
        
    return cadena_invertida

def mostrar_contrasenia_invertida(contrasenia: str):
    """
    muestra por pantalla la contraseña invertida utilizando la función auxiliar.
    """
    invertida = invertir_cadena(contrasenia)
    print(f"\nLa contraseña invertida es: {invertida}")

def ordenar_contrasenia(contrasenia: str):
    """
    ordena la cadena por código ASCII trabajando solo con strings.
    """
    longitud = len(contrasenia)
    cadena_ordenada = contrasenia
    
    for i in range(longitud - 1):
        for j in range(longitud - 1 - i):
            
            if cadena_ordenada[j] > cadena_ordenada[j + 1]:        
                
                nueva_cadena = ""
                
                for k in range(longitud):
                    if k == j:
                        nueva_cadena = nueva_cadena + cadena_ordenada[j + 1]
                    elif k == j + 1:
                        nueva_cadena = nueva_cadena + cadena_ordenada[j]
                    else:
                        nueva_cadena = nueva_cadena + cadena_ordenada[k]
                cadena_ordenada = nueva_cadena

    print("\n--- Contraseña Ordenada ---")
    print(f"Original: {contrasenia}")
    print(f"Ordenada: {cadena_ordenada}")