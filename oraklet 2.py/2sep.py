import random

while True: 
    ssp = ["sten", "sax", "påse"]
    slag = input("sten, sax, påse? ").strip()
    datorns_slag = random.choice(ssp)

    if slag == datorns_slag:
        print("ingen vann")
    elif slag == ("sten") and datorns_slag == ("sax"):
        print("du vann")
        break
    elif slag == ("sax") and datorns_slag == ("påse"):
        print("du vann")
        break
    elif slag == ("sten") and datorns_slag == ("påse"):
        print("du förlorade!")
        break
    elif slag == ("påse") and datorns_slag == ("sten"):
        print("du vann!")
        break
    elif slag == ("sten") and datorns_slag == ("påse"):
        print("du förlorade!")
        break
    elif slag == ("sax") and datorns_slag == ("sten"):
        print("du förlorade!")
        break
    elif slag == ("påse") and datorns_slag == ("sax"):
        print("du förlorade!")
        break