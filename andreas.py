import random

def randomizerGrp():

    listen = []

    while(len(listen) < 8):
        rnd = random.randint(1,8)
        if rnd not in listen:
            listen.append(rnd)

    return listen

print (randomizerGrp())
