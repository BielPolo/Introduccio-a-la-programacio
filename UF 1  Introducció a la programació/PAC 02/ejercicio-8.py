frase = input("Dime una frase: ")
letra = input("Dime una letra: ")

contador = 0
for x in frase:
    if x == letra:
        contador += 1

print("La letra que has introducido aparece " + str(contador) + " veces")