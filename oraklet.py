
import random

svar = ["ja det är klart.", "Aldrig i livet", "jag fattar inte frågan.", "vill du verkligen veta."]

fråga = input("fråga oraklet: ")
print("Du frågade:", fråga)
print(random.choice(svar))