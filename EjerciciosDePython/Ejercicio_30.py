
lista = [10, 21, 34, 45, 50, 67, 80, 99, 100]
pares = []
impares = []

for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Números pares:", pares)
print("Números impares:", impares)