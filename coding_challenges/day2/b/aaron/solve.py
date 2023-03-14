import math

results = []

n = int(input())
for i in range(n):
    vals = input().split()
    r = int(vals[0])
    a = float(vals[1])
    est_pi = a/float(r**2)
    err = abs(math.pi - est_pi)
    results.append((err, r))

sorted_results = sorted(results, key=lambda x: x[0])
product = 1
for val in sorted_results[:5]:
    product *= val[1]

print(product)
