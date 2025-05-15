numero1 = float(input("\nIngrese el nuemro 1: "))
numero2 = float(input("\nIngrese el nuemro 2: "))
caracter = input("\nCual operacion desea realizar, elija un simbolo: (+, -, *, /): ")

if caracter == '+':
    resultado = numero1 + numero2
    print(resultado)
elif caracter == '-':
    resultado = numero1 - numero2
    print(resultado)
elif caracter == '*':
    resultado = numero1 * numero2
    print(resultado)
elif caracter == '/':
    resultado = numero1 / numero2
    print(resultado)
else:
    print("\nNo esxiste operador")