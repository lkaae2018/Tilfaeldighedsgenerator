import random
import time

n = 0  # Tæller til at tælle hvormange tal der bliver lagt i liste med tilfældigetal
tiltal = [0, 0, 0, 0, 0, 0, 0, 0]  # De 8 tal til grupperne
samme = 0  # Samme=0 betyder at der er et nyt tal til listen, samme=1 der findes et tal forvejen
tal =0
#tal = random.randint(1, 8)  # Det første tal genereres til listen
#print(tal)
#tiltal.insert(n, tal)
# n += 1

while True:

    samme = 0
    time.sleep(1)
    tal = random.randint(1, 8)
    print("tal=:" + str(tal))

    for m in range(7):  # Undersøger om det nye tal er allerede i listen
        if tiltal[m] == tal:
            samme = 1  # Samme sættes til 1 hvis tal er i listen

    if samme == 0:  # Hvis samme = 0 skal tallet lægges i listen tiltal
        tiltal.insert(n, tal)
        print("n=: " + str(n))
        print("tal lagt i liste " + str(tiltal[n]))
        print(tiltal)
        n += 1

    if n == 8:  # Når de 8 tal er fundet skal listen udskrives og program stopper
        for tt in range(8):
            print(tiltal[tt])
        break
