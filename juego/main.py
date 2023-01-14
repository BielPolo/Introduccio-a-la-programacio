import random

words = ["silla", "mesa", "escritorio"]
playing = True
lives = 5

word = random.choice(words)
word = list(word)

print("la palabra a adivinar contiene " + str(len(word)) + " letras")

def check(lives):
    letra = input("dime una letras: ")
    if letra in word:
        print("sigue asi")
    else:
        print("te has equivocado")
        lives = lives -1
    return lives

while playing:
    lives = check(lives)
    playing = lives != 0

    if playing:
        print("tienes " + str(lives) + " vidas")
    else:
        print("Has perdido")





