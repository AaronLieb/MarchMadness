import random
import numpy as np
import locale

locale.setlocale( locale.LC_ALL, '' )

DEBUG = False

MIN_CHECKS = 10000
MAX_CHECKS = 20000
NUM_BRACKETS = 50
MIN_MULT = 1.1
MAX_MULT = 1.34

if DEBUG:
    MIN_CHECKS = 22
    MAX_CHECKS = 22
    NUM_BRACKETS = 8
    MIN_MULT = 1.5
    MAX_MULT = 3.0

MIN_PAY = 1
MAX_PAY = 100000

MIN_INITIAL = 5000
MAX_INITIAL = 15000


n = random.randint(MIN_CHECKS, MAX_CHECKS)

brackets = [random.randint(MIN_INITIAL, MAX_INITIAL)]

def money(money):
    return locale.currency(money, grouping=True)[:-3]

def percent(num):
    return str(int(num*100)) + "%"


print(NUM_BRACKETS + 1)
print(n)

print(money(0), money(brackets[0] - 1), percent(0))
for i in range(NUM_BRACKETS):
    brackets.append(int(brackets[i] * random.uniform(MIN_MULT, MAX_MULT)))
    print(money(brackets[i]), money(brackets[i + 1] - 1), percent(((i + 1)/NUM_BRACKETS)**(7/10)))

for i in range(n):
    amount = abs(np.random.normal(0, 10000, size=(1))[0])
    print(money(amount))

