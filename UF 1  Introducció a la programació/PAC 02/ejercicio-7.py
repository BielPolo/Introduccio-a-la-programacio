listaNombres = ["azul", "rojo", "verde", "amarillo", "negro"]

palabra = input("dime una palabra: ")

posicion = None
for index, nombre in enumerate(listaNombres):
    if nombre == palabra:
        posicion = index
        break

if posicion != None:
    print("La palabra " + str(palabra) + " se encuentra en la posicion " + str(posicion) + " de la lista")
else:
    print("La palabra que has introducido no se encuentra en la lista")
