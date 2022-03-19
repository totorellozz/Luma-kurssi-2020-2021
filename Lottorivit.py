import random

voittorivi = []

while len(voittorivi) < 7:
    numero = random.randint(1, 40)
    if numero not in voittorivi:
        voittorivi.append(numero)

voittorivi.sort()

riveja = int(input("montako riviä pelataan?: "))
for x in range(riveja):
    pelirivi = []

    while len(pelirivi) < 7:
        numero = random.randint(1, 40)
        if numero not in pelirivi:
            pelirivi.append(numero)

    pelirivi.sort()
    print(pelirivi)

    if pelirivi == voittorivi:
        print("voitit")
        break


