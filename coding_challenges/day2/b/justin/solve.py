n = int(input())

PI = 3.141592653589793  # 15 digits

area = lambda r: PI * (r**2)

errors = []

# area = PI * r^2
# PI = area/r^2

for _ in range(n):
    rr, ra = input().split()
    r = int(rr)
    a = float(ra)
    actual_area = area(r)
    # error = abs(actual - a)
    their_pi = a / (r**2)
    error = abs(their_pi - PI)
    errors.append((r, error))

# now sort the errors by [1]

best = sorted(errors, key=lambda x: x[1])
ans = 1
for b in best[:5]:
    ans *= b[0]
print(ans)
