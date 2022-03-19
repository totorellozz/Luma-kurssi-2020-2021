
print("valitse seuraavista: ")
a = float(input("ilmoita korkeus: "))
aa = float(input("ilmoita leveys: "))

b = float(input("ilmoita korkeus/leveys: "))

r = float(input("ilmoita säde: "))

if a == None:
    pass
else:
    # toim = a * aa
    # toim = toim / 2
    print("kolmion pinta-ala:", a * aa / 2)

if b == None:
    pass
else:
    # toim1 = b * b
    print("suorakolmion pinta-ala:", b * b)

if r == None:
    print("nnn")
else:
    # toim2 = "r / 2"
    print("ympyrän pinta-ala:", r / 2)
