import random
import time

n = 1

while True:
    noppa1 = random.randint(1, 6)
    print("Noppa1 on: ", noppa1)
    # time.sleep(0.5)
    noppa2 = random.randint(1, 6)
    print("Noppa2 on: ", noppa2)
    # time.sleep(0.5)
    noppa3 = random.randint(1, 6)
    print("Noppa3 on: ", noppa3)
    # time.sleep(0.5)
    noppa4 = random.randint(1, 6)
    print("Noppa4 on: ", noppa4)
    # time.sleep(0.5)
    noppa5 = random.randint(1, 6)
    print("Noppa5 on: ", noppa5)
    if noppa1 == noppa2 == noppa3 == noppa4 == noppa5:
        print("Onneksi olkoon, voitit!")
        break
    else:
        print("Kierros: ")
        print(n)
        n += 1
        # time.sleep(2)
