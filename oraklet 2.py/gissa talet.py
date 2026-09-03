import random
tal =random.randint( 1, 10)
guess = int(input("gissa ett tal mellan 1 och 10"))
Antalg = int(0)

while True:
    if guess == tal:
        print("DU GISSADE RÄTT!!!")
        break
    elif guess < tal:
        print ("du gissade för lågt, testa igen")
        guess = int(input("gissa ett tal mellan 1 och 10: "))
    elif guess > tal:
        print ("du gissade för högt, testa igen")
        guess = int(input("gissa ett tal mellan 1 och 10 :"))
    Antalg +=1
    print (f"Antal gissningar = {Antalg}")