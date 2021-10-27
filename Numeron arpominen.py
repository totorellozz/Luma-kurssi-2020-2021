import random

numero = int(input('Kirjoita numero:'))
noppa = (random.randint(1, 1))

if numero == noppa:
    print('Arvasit!')
else:
    print("Numero on suurempi") if numero > noppa else print("Numero on pienempi")
