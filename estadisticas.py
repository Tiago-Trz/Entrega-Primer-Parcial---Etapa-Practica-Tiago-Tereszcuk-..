def generar_reporte(contrasenia: str):
    """
    calcula y muestra la longitud total, los porcentajes de cada tipo de carácter 
    y la cantidad de caracteres que se repiten consecutivamente.
    """
    longitud = len(contrasenia)
    letras = 0
    numeros = 0
    simbolos = 0
    consecutivos = 0

    # 1. cuenta para sacar los porcentajes
    for indice in range(longitud):
        caracter = contrasenia[indice]
        if (caracter >= 'a' and caracter <= 'z') or (caracter >= 'A' and caracter <= 'Z'):
            letras = letras + 1
        elif caracter >= '0' and caracter <= '9':
            numeros = numeros + 1
        elif caracter >= '!' and caracter <= '/':
            simbolos = simbolos + 1

    # 2. busca caracteres repetidos consecutivos
    for indice in range(longitud - 1):
        if contrasenia[indice] == contrasenia[indice + 1]:
            consecutivos = consecutivos + 1

    # 3. calcula los porcentajes
    porc_letras = (letras * 100) / longitud
    porc_numeros = (numeros * 100) / longitud
    porc_simbolos = (simbolos * 100) / longitud

    print("\n--- Reporte Estadístico ---")
    print(f"Longitud total: {longitud} caracteres")
    print(f"Porcentaje de letras: {porc_letras}%")
    print(f"Porcentaje de números: {porc_numeros}%")
    print(f"Porcentaje de símbolos: {porc_simbolos}%")
    print(f"Caracteres repetidos consecutivos: {consecutivos}")