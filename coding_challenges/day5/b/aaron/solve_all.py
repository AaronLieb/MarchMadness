from functools import lru_cache
import math
import sys

sys.setrecursionlimit(100000)

MODDY = 10**7+7

@lru_cache(maxsize = 99999)
def gnacci(g, index):
    if index == 1:
        return 0
    if index <= g:
        return 1
    sum = 0
    for i in range(g):
        sum += gnacci(g, index - i - 1) % MODDY
    return sum % MODDY

sieve_size = 10**7 + 8
nums = [True]*sieve_size
for i in range(2, math.ceil(math.sqrt(sieve_size))):
    if not nums[i]:
        continue
    for j in range(i**2, sieve_size, i):
        nums[j] = False

primes = []
for i in range(2, len(nums)):
    if nums[i]:
        primes.append(i)

primes = set(primes)

def solve(lines):
    n, k = [int(x) for x in lines.pop(0).split()]
    accounts = {}
    taxable_income = {}
    for i in range(n):
        g, v = [int(x) for x in lines.pop(0).split()]
        account = gnacci(g, v)
        taxable_income[account] = 0
        accounts[account] = (g, v)

    for i in range(k):
        a, _, b, money = lines.pop(0).split()
        a = int(a)
        b = int(b)
        money = int(money[2:-1])
        if money not in primes:
            taxable_income[b] += money

    max_account = None
    max_income = 0
    for account, income in taxable_income.items():
        if income > max_income:
            max_account = account
            max_income = income

    og = accounts[max_account]
    print(''.join([str(x) for x in og]))

if __name__ == '__main__':
    for i in range(100):
        filename = "../inputs/" + str(i) + ".in"
        with open(filename) as f:
            lines = f.readlines()
            solve(lines)

