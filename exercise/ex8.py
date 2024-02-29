# Program returns a random number that falls between the two whole numbers

import random

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

result = random.randint(lower_bound, upper_bound + 1)

print(result)
