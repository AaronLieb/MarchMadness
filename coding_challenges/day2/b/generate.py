import math
import random

DEBUG = True

MIN_PEOPLE = 10000
MAX_PEOPLE = 20000

if DEBUG:
    MIN_PEOPLE = 10
    MAX_PEOPLE = 10

n = random.randint(MIN_PEOPLE, MAX_PEOPLE)

precision = 15

print(n)
for i in range(n):
    r = random.randint(10, 20)
    pi = round(random.uniform(2.0, 4.0), precision)
    a = pi * r**2
    print(r, a, pi)

