edad = int(input("dime tu edad: "))

if edad >= 5 and edad <= 13:
    print("Estas en la niñez")

elif edad >= 14 and edad <= 17:
    print("Estas en estas en la adolescencia")

elif edad >= 18 and edad <= 35:
    print("Estas en adultos jovenes")

elif edad >= 36 and edad <= 64:
    print("Estas en adultos")

elif edad >= 65:
    print("Estas en la tercera edad")