# Define a function, random_number, that takes no parameters. The function must generate a random integer between 1 and 100, both inclusive, and return it.
# Calling the function multiple times should (usually) return different numbers.
# For example, calling random_number() some times might first return 42, then 63, then 1.

from random import randrange

def random_number(lower, upper):
    rand = randrange(int(lower), int(upper))
    return rand

print(random_number(input("insert lower: "), input("insert upper: ")))
