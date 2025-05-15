edad = int(input("\nIngrese una edad: "))

if 0 <= edad <= 11:
    print("\nNiño")
elif 12 <= edad <= 25:
    print("\nAdolecente")
elif 26 <= edad <= 60:
    print("\nAdulto")
else:
    print("\nAnciano")
    