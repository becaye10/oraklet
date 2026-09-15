import random
import time

fsld = ditt_första_slag = random.randint(1, 6)
ditt_andra_slag = random.randint(1, 6)

datorns_första_slag = random.randint(1, 6)
datorns_andra_slag = random.randint(1, 6)

print("ditt första tal är", ditt_första_slag)

time.sleep(1)

theonurse = input( "vill du stanna eller köra igen? ")

P1 = datorns_första_slag + ditt_andra_slag
P2 = ditt_första_slag + ditt_andra_slag


if theonurse == "kör igen":
    print ("ditt andra slag är", ditt_andra_slag)
    time.sleep(1)
    print ("du har totalt", ditt_första_slag + ditt_andra_slag)
    time.sleep(2)
else:
    print ("du stannade och fick totalt", ditt_första_slag)
    time.sleep(1)

print("Och datorns första slag är", datorns_första_slag)
time.sleep(1)

if datorns_första_slag <6:
    print ("datorns andra slag är", datorns_andra_slag)
    time.sleep(1)
    print ("datorn fick totalt", datorns_första_slag + datorns_andra_slag)
    time.sleep(1)

else:
    print ("datorn stannar")
    time.sleep(1)
    print ("datorn fick totalt", datorns_första_slag)
    time.sleep(2)
    print

print ("du har totalt", P2)
time.sleep(1)
 


if P1 > 10:
    print("Du gick över 10 och förlorade")    
elif 10-P1 < 10-P2:
    print ("Grattis du var närmare 10 och vann!")
elif 12 - P1> 10 - P2:
    print("Datorn var närmare så du förlorade!")
elif P1 == P2:
    print("det blev lika") 