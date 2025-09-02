# ===============================
# Código base en Python
# ===============================

# Función principal
def main():
    print("¡Hola! Este es un código base en Python.")
    
    # Ejemplo de variables
    nombre = "Usuario"
    edad = 20
    
    # Ejemplo de condicional
    if edad >= 18:
        print(f"{nombre} es mayor de edad.")
    else:
        print(f"{nombre} es menor de edad.")
    
    # Ejemplo de bucle
    for i in range(5):
        print(f"Iteración número: {i+1}")
    
    # Ejemplo de función
    resultado = sumar(5, 7)
    print(f"La suma de 5 + 7 es: {resultado}")


# Función adicional
def sumar(a, b):
    return a + b


# Punto de entrada
if __name__ == "__main__":
    main()
