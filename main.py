def convertir_numeros(decimal):
    binario = bin(decimal)[2:] 
    octal = oct(decimal)[2:]    
    hexadecimal = hex(decimal)[2:].upper()  

    print(f"Decimal: {decimal}")
    print(f"Binario: {binario}")
    print(f"Octal: {octal}")
    print(f"Hexadecimal: {hexadecimal}")

def main():
    while True:
        try:
            numero_decimal = int(input("Introduce un número decimal (o -1 para salir): "))
            if numero_decimal == -1:
                print("Saliendo del programa. ¡Hasta luego!")
                break
            convertir_numeros(numero_decimal)
            print("\n")
        except ValueError:
            print("Por favor, introduce un número válido.\n")

if __name__ == "__main__":
    main()
