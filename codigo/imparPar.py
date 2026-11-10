numeros = []
pares = []
impares = []

while True:
    try:
        cantidad = int(input("¿Cuántos números querés ingresar?: "))
        if cantidad > 0:
            break
        print("El valor debe ser mayor a 0.")
    except ValueError:
        print("Error: Ingrese un número entero válido.")

for i in range(cantidad):
    while True:
        try:
            n = int(input(f"Ingrese el número {i+1}: "))
            break
        except ValueError:
            print("Error: Ingrese un número entero válido.")
    
    numeros.append(n)
    
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("\n--- RESULTADOS ---")
print(f"Lista completa: {numeros}")
print(f"Números pares ({len(pares)}): {pares} - Suma total: {sum(pares)}")
print(f"Números impares ({len(impares)}): {impares} - Suma total: {sum(impares)}")
