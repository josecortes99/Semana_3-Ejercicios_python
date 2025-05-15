numero1 = int(input("\nIngrese un numero 1: "))
numero2 = int(input("\nIngrese un numero 2: "))
numero3 = int(input("\nIngrese un numero 3: "))

if numero1 > numero2 and numero1 > numero3:
    print("\nNumero uno mayor")
elif numero1 < numero2 and numero2 > numero3:
    print("\nNumero dos mayor")
elif numero1 < numero3 and numero3 > numero2:
    print("\nNumero tres mayor")
else:
    print("\nhay numeros iguales ")