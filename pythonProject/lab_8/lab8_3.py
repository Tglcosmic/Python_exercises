import random

with open("random_numbers.txt", "w") as file:
    for _ in range(1000000):
        random_number = random.randint(0, 100)
        file.write(str(random_number) + " ")
