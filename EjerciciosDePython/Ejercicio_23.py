calificaciones = []  

while True:
    entrada = input("Ingrese una calificación (o escriba 'fin' para terminar): ")

    if entrada.lower() == "fin": 
        break

    try:
        calificacion = float(entrada)  
        calificaciones.append(calificacion)
    except ValueError:
        print("Entrada inválida. Ingrese un número o 'fin'.")

if calificaciones: 
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"\n{promedio:.2f}")
else:
    print("\nNo se ingresaron calificaciones válidas.")