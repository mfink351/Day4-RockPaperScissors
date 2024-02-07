import random

names = input("Enter a list of names: ").split(", ")

#Choice2 Solution
print(f"{random.choice(names)} is going to pay the bill.")

#RandInt Solution
print(f"{names[random.randint(0, len(names)-1)]} is going to pay the bill.")