suma_total = 0
while True:
    entrada = input("Ingrese un número (o escriba 'fin' para terminar): ")
    
    if entrada.lower() == "fin":
        break
    
    try:
        suma_total += float(entrada)
    except ValueError:
        print("Entrada inválida. Ingrese un número o 'fin'.")

print(suma_total)