def conversor():
    print("CONVERSOR DE UNIDADES")
    print("Opciones disponibles:")
    print("1. Divisas")
    print("2. Peso")
    print("3. Tamaño de archivos")
    print("4. Temperatura")
    print("5. Distancia")
    print("0. Salir")

    while True:
        opcion = input("\nElige una opción (0-5): ")

        if opcion == "0":
            print("Hasta luego!")
            break

        elif opcion == "1":
            divisas()

        elif opcion == "2":
            peso()

        elif opcion == "3":
            archivos()

        elif opcion == "4":
            temperatura()

        elif opcion == "5":
            distancia()

        else:
            print("Opción no válida, intenta de nuevo.")


#Divisas
def divisas():
    # tasas actuales aproximadas ARS a dia 24/09/2025 → otras
    tasas = {
        "ARS": 1,
        "USD": 1 / 1367.50,   # si tenés X ARS, cuántos USD
        "EUR": 1 / 1606.43,
        "GBP": 1 / 1826.49,
        "JPY": 1 / 9.25
    }

    print("\nConversor de Divisas (base ARS)")
    try:
        cantidad = float(input("Ingresa la cantidad en Pesos Argentinos: "))
    except ValueError:
        print("Debes ingresar un número válido.")
        return

    for moneda, tasa in tasas.items():
        convertido = cantidad * tasa
        print(f"{cantidad} ARS = {convertido:.2f} {moneda}")


#Peso
def peso():
    unidades = {
        "gramos": 1000,           # 1 kg = 1000 gramos
        "kilogramos": 1,          # Base
        "libras": 2.20462,        
        "onzas": 35.274,         
        "toneladas": 0.001        
    }

    print("\nConversor de Peso")
    try:
        cantidad = float(input("Ingresa la cantidad en kilogramos: "))
    except ValueError:
        print("Debes ingresar un número válido.")
        return

    for unidad, factor in unidades.items():
        convertido = cantidad * factor
        print(f"{cantidad} kg = {convertido:.2f} {unidad}")



#Tamaño de archivos
def archivos():
    unidades = {
        "bytes": 1024 ** 2,        
        "kilobytes": 1024,          # 1 MB = 1024 KB
        "megabytes": 1,             # Base
        "gigabytes": 1 / 1024,      
        "terabytes": 1 / (1024 ** 2) 
    }

    print("\nConversor de Tamaño de Archivos")
    try:
        cantidad = float(input("Ingresa la cantidad en megabytes: "))
    except ValueError:
        print("Debes ingresar un número válido.")
        return

    for unidad, factor in unidades.items():
        convertido = cantidad * factor
        print(f"{cantidad} MB = {convertido:.3f} {unidad}")


#Temperatura
def temperatura():
    print("\nConversor de Temperatura")
    try:
        celsius = float(input("Ingresa la temperatura en Celsius: "))
    except ValueError:
        print("Debes ingresar un número válido.")
        return

    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15

    print(f"{celsius} °C = {fahrenheit:.2f} °F")
    print(f"{celsius} °C = {kelvin:.2f} K")


#Distancia
def distancia():
    unidades = {
        "metros": 1,
        "centimetros": 100,        # 1 metro = 100 centímetros
        "pulgadas": 39.3701,        # 1 metro ≈ 39.3701 pulgadas
        "kilometros": 0.001,
        "millas": 0.000621371,
        "yardas": 1.09361,
        "pies": 3.28084
    }

    print("\nConversor de Distancia")
    try:
        cantidad = float(input("Ingresa la cantidad en metros: "))
    except ValueError:
        print("Debes ingresar un número válido.")
        return

    for unidad, factor in unidades.items():
        convertido = cantidad * factor
        print(f"{cantidad} metros = {convertido:.2f} {unidad}")


# Ejecutar el programa
if __name__ == "__main__":
    conversor()