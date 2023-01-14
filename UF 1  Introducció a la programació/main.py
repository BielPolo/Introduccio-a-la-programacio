numero7 = int(input("N. de cliente:"))

if numero7 == 1000:
    print("Ganaste un premio!")
elif numero7 >= 500:
    print("ganastes 75%")
elif 500 > numero7 > 250:
    print("ganastes 50%")
else:
    print("no ganastes nada")