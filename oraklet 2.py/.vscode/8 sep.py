import random
import time

fsld = ditt_första_slag = random.randint(1, 6)
ditt_andra_slag = random.randint(1, 6)

datorns_första_slag = random.randint(1, 6)
datorns_andra_slag = random.randint(1, 6)

print("ditt första tal är", ditt_första_slag)

time.sleep(1)

theonurse = input( "vill du stanna eller köra igen? ")

P2 = datorns_första_slag + datorns_andra_slag
P1 = ditt_första_slag + ditt_andra_slag


if theonurse == "kör igen":
    print ("ditt andra slag är", ditt_andra_slag)
    time.sleep(1)
    print ("du har totalt", ditt_första_slag + ditt_andra_slag)
    time.sleep(2)
elif P1 > 10:
    print("Du gick över 10 och förlorade") 
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
elif P2 > 10:
    print("Datornn gick över 10 och du vann!")
else:
    print ("datorn stannar")
    time.sleep(1)
    print ("datorn fick totalt", datorns_första_slag)
    time.sleep(2)
    print

print ("och du har totalt", P1)
time.sleep(1)
 

if P2 == P1:
    print("det blev lika")
elif 10-P1 < 10-P2:
    print ("Grattis du var närmare 10 och vann!")
elif 10 - P1 > 10 - P2:
    print("Datorn var närmare så du förlorade!")