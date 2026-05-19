import analisis
import estadisticas
import utilidades
import validaciones

def mostrar_menu():
    """
    Muestra las opciones del menu principal en pantalla
    """
    print("\n--- Sistema de Procesamiento de Contraseñas ---")
    print("1. Ingresar contraseña")
    print("2. Validar nivel de seguridad")
    print("3. Contar tipos de caracteres")
    print("4. Buscar caracter especifico")
    print("5. Mostrar contraseña invertida")
    print("6. Gererar reporte estadistico")
    print("7. Verificar si es palindromo")
    print("8. Ordenar caracteres de la contraseña")
    print("9. Salir")

def main():
    # inicio la variable fuera del bucle
    contrasenia = ""
    opcion = ""

    # con este bucle while hago continuar el programa hasta la opcion 9
    while opcion != "9":
        mostrar_menu()
        opcion = input("Ingresa una opción (1-9): ")

        if opcion == "1":
            contrasenia = validaciones.ingresar_contrasenia()
        
        elif opcion == "2":
            if contrasenia == "":
                print("ERROR: Primero ingresa tu contraseña (opción 1).")
            else:
                nivel = validaciones.validar_seguridad(contrasenia)
                print(f"El nivel de seguridad de la contraseña es: {nivel}")
        
        elif opcion == "3":
            if contrasenia == "":
                print("Error: Primero debe ingresar una contraseña (Opción 1).")
            else:
                analisis.contar_tipos_caracteres(contrasenia)     
        
        elif opcion == "4":
            if contrasenia == "":
                print("Error: Primero debe ingresar una contraseña (Opción 1).")
            else:
                analisis.buscar_caracter(contrasenia)
        
        elif opcion == "5":
            if contrasenia == "":
                print("Error: Primero debe ingresar una contraseña (Opción 1).")
            else:
                utilidades.mostrar_contrasenia_invertida(contrasenia)
        
        elif opcion == "6":
            if contrasenia == "":
                print("Error: Primero debe ingresar una contraseña (Opción 1).")
            else:
                estadisticas.generar_reporte(contrasenia)
        
        elif opcion == "7":
            if contrasenia == "":
                print("Error: Primero debe ingresar una contraseña (Opción 1).")
            else:
                analisis.verificar_palindromo(contrasenia)
                
        elif opcion == "8":
            if contrasenia == "":
                print("Error: Primero debe ingresar una contraseña (Opción 1).")
            else:
                utilidades.ordenar_contrasenia(contrasenia)
        
        elif opcion == "9":
            print("¡Nos vemos! Saliendo del programa...")
        
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 9.")

# llamo a mi función principal para que arranque el programa
main()
