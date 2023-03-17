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

print(gnacci(3, 12))
