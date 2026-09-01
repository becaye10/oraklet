import random

ditt_slag = random.randint(1, 10)
datorns_slag = random.randint(1, 10)

print(f"du slog:{ditt_slag}")
print(f"datorn slog:{datorns_slag}")

if ditt_slag > datorns_slag:
    print("du vann!")
else:
    print("datorn vann!")    
