R = int(input("(kirjoita näistä vain 2)resistanssi: "))
U = int(input("(kirjoita näistä vain 2)jännite: "))
I = int(input("(kirjoita näistä vain 2)sähkövirta: "))

if R == 0:
    R = 1
    resistanssi = R = U / I
else:
    resistanssi = R = U / I

if U == 0:
    U = 1
    jännite = U = R / I
else:
    jännite = U = R / I

if I == 0:
    I = 1
    sähkövirta = I = U / R
else:
    sähkövirta = I = U / R

print("resistanssi:", resistanssi)
print("jännite:", jännite)
print("sähkövirta:", sähkövirta)



