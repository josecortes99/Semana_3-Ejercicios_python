
lista = [10, 25, 3, 50, 7, 98, 45]

mayor = lista[0]
menor = lista[0]

for num in lista:
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
