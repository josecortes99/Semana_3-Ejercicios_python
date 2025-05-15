
numero = int(input("Ingrese un número: "))

factorial = 1
for i in range(1, numero + 1):
    factorial *= i  # Multiplicamos cada número en la secuencia

print(f"\nEl factorial de {numero} es: {factorial}")