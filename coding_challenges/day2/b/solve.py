import math

n = int(input())
for i in range(n):
    vals = input().split()
    r = int(vals[0])
    a = float(vals[1])
    est_pi = a/(r**2)
    err = abs(math.pi - est_pi)
    print(err, est_pi)
