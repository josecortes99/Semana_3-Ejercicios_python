
    
Año = int (input ("\nIngrese un año: "))

if (Año % 4 == 0 and Año % 100 != 0) or (Año % 400 == 0):
    print ("\nEl año es bisiesto")
    
else:
    print ("\nEl año no es bisiesto")