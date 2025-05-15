flag = True
while flag:
    num =int(input("\nAdivina el numero: "))
    nume = 7
    if num == nume:
        print("\nAdivinaste")
        flag = False
    elif num < nume:
        print("\nEl numero ingresado es menor")
    else:
        print("\nEl numero ingresado es mayor")
