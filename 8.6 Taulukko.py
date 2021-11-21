taulukko = []

x = int(input("Monta asiaa haluat laittaa listaan? : "))

for i in range(x):
    lst = input("Kirjoit asiat: ")

    taulukko.append(lst)

print('\n'*25)

for taulukko in taulukko:
    print(taulukko)
