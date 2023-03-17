from random import randint, choice
import sys
from collections import defaultdict

from util import kNacci, getNacciPair, sieve, MOD
'''
3 5 (number of bank accounts, number of transactions, !!prime numbers not taxed)
[0] 4 17
[1] 2 100
[2] 5 11
<keep k-nacci below 7 but above or equal to 2>
<transaction history, find out what bank account number made the most taxable income mod 10**9 + 7>
15123123 -> 12451231 ($317) (if prime don't count it) (they need to know that 15123123 is some k-nacci)
12312565134 -> 12451231 ()

write the account number who made the most taxable income (primes are not TAXED!)
# (how much taxable income did 12451231 make)
# (keep numbers below 2^62)
'''
DEBUG = False
if DEBUG:
    print(f"<<DEBUG MODE ON>>")

N, K, naccis, solved_naccis, chosen, primes, primes_lookup, incomes, calculated_naccis = [None] * 9
primes = sieve()
primes_lookup = set(primes)

def getMeta():
    global N, K, naccis, solved_naccis, chosen, primes, primes_lookup, incomes, calculated_naccis
    N = 8 if DEBUG else randint(2000, 3333)
    K = 40 if DEBUG else randint(11_000, 20_000)
    naccis = list(set([getNacciPair() for _ in range(N)])) # set->list cast to remove dupes
    N = len(naccis) # reset N to the number after removing dupes
    assert len(naccis), 'empty naccis!'
    solved_naccis = [kNacci(x[0], x[1]) for x in naccis]
    assert len(solved_naccis) == len(naccis), 'Uh-oh, solved naccis not same length as generated naccis'
    solved_naccis_no_dupes = set(solved_naccis)
    # print(solved_naccis, '\n', solved_naccis_no_dupes)
    assert len(solved_naccis) == len(solved_naccis_no_dupes), 'Uh-oh, multiple nacci pairs hit same routing number'
    chosen = set()
    incomes = defaultdict(lambda: int()) # not used for generator, this is for solver
    calculated_naccis = {v: ''.join([str(x) for x in k]) for k, v in zip(naccis, solved_naccis)}
    # print('naccis', naccis)
    # print('solved_naccis', solved_naccis)
    # print('calculated_naccis', calculated_naccis)

# print(naccis)
# print(solved_naccis)


def generateTransaction():
    global N, K, naccis, solved_naccis, chosen, primes, primes_lookup, incomes, calculated_naccis
    # pick two random solved_naccis
    n1 = choice(solved_naccis) # from
    n2 = n1 # to
    while n2 == n1: # ensure different bank accounts
       n2 = choice(solved_naccis)

    # generate amount ($xxx) make prime 13% of the time
    r = randint(0, 99)
    val = 3
    chose_prime = False
    if r <= 13: # pick a random prime greater than 11597
        prime = choice(primes[1000:])
        val = prime
        chose_prime = True
    else:
        while val in primes_lookup:
            val = randint(4, MOD) # guarantee non prime
    incomes[n2] += val if not chose_prime else 0
    return f"{n1} -> {n2} (${val})"

def generateOne():
    global N, K, naccis, solved_naccis, chosen, primes, primes_lookup, incomes, calculated_naccis
    getMeta()
    out = f"{N} {K}\n"
    # print(N, K)
    # print bank account numbers
    for nacci in naccis:
        out += f"{nacci[0]} {nacci[1]}\n"
        # print(nacci[0], nacci[1])

    # print transactions
    for _ in range(K):
        out += generateTransaction() + "\n"
        # print(generateTransaction())

    highest = [None, -1]
    for id, amnt in incomes.items():
        if amnt > highest[1]:
            highest[1] = amnt
            highest[0] = id
    err = str(calculated_naccis[highest[0]]) + "\n"
    return out, err
    # print(calculated_naccis[highest[0]], file=sys.stderr)

if __name__ == '__main__':
    ans = generateOne()
    print(ans[0], '\n', ans[1], sep='')
