
import time

numero = int(input("Ingrese un número para la cuenta regresiva: "))

print("\nIniciando cuenta regresiva...\n")
for i in range(numero, 0, -1): 
    print(i)
    time.sleep(1) 

print("\nTiempo cumplido")