from random import randint
NACCI_COEFF = 9000
MOD = 10**7+7 # TODO: increase for prod (to 7)

def getNacciPair():
    degree = randint(2, 9)
    idx = randint(NACCI_COEFF//degree, NACCI_COEFF//degree * 2)
    return (degree, idx)

def kNacci(k: int, idx: int) -> int:
    prev = [0] + [1] * (k - 1) + [0] * idx
    if idx < k: return prev[idx-1]

    i = k
    while i < idx:
        s = 0
        for num in prev[i-k:i]:
            s += (num % MOD)
        prev[i] = s
        i += 1

    return prev[idx-1] % MOD

def sieve(n: int = MOD+1) -> list[int]:
    nums = [True] * n # assume all are primes
    for i in range(2, n):
        for j in range(i*2, n, i):
            nums[j] = False
    return [idx for idx in range(len(nums)) if nums[idx] is True]

if __name__ == '__main__':
    print(kNacci(2, 10))
    # print(kNacci(2, 1))
    # print(kNacci(2,99))
    # for i in range(1, 20):
    #     print(kNacci(2, i))
    # print(kNacci(2, 2))
    # print(sieve(6000))
