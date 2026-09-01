
name = input ("name")
age = int(input ("age"))
print (( name +str(age)))
print(" om ett år blir du " + str(age + 1))
guess = int(input("gissa ett tal mellan 1 och 10"))
if guess == 5:
    print("du gissade rätt!")
if guess < 5:
    print("du gissade för lågt")
if guess > 5:
    print("du gissade för högt")
