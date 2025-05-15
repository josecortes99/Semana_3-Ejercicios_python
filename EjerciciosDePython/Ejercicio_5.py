calificacion = float(input("\nIngrese una calificacion de 1 a 10: "))
if calificacion in range(10):
    if calificacion >= 6:
        print("\nGano")
    else:
        print("\nPerdio")
else:
    print("\nNo valida")