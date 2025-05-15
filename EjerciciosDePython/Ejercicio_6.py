numero = int(input("\nIngrese un numero: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("\nSon divisibles por los dos")
elif numero % 3 == 0:
    print("\nEs divisible por tres")
elif numero % 5 == 0:
    print("\nEs divisible por cinco")
else:
    print("\nNo es divisible ")