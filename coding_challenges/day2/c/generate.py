import random

DEBUG = True

MIN_LOCATIONS = 20
MAX_LOCATIONS = 20

if DEBUG:
    MIN_LOCATIONS = 10
    MAX_LOCATIONS = 10

n = random.randint(MIN_LOCATIONS, MAX_LOCATIONS)

X_RANGE = 2000
Y_RANGE = 2000

print(n)
for i in range(n):
    x = random.randint(-X_RANGE, X_RANGE)
    y = random.randint(-Y_RANGE, Y_RANGE)
    print(x, y)


