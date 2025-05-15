
numeros = [] 

while True:
    entrada = input("Ingrese un número (o escriba 'fin' para terminar): ")
    
    if entrada.lower() == "fin":  
        break
    
    try:
        numeros.append(float(entrada))  
    except ValueError:
        print("Entrada inválida. Ingrese un número o 'fin'.")

numeros.sort()  

print("\nLista ordenada:", numeros)