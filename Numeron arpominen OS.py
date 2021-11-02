import random
import os

numero = int(input('Kirjoita numero: '))
noppa = (random.randint(1, 10))

while True:
    if numero == noppa:
        print('Arvasit', os.getlogin(), '\U0001F601 \U0001F91F \U0001F44D \U0001F44F')
        break
    else:
        print("Numero on suurempi") if numero < noppa else print("Numero on pienempi")
        numero = int(input('Yritä uudelleen \U0001F625: '))

