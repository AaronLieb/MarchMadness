import math
n = int(input())

points = []

for i in range(n):
    points.append([float(x) for x in input().split()])

min_d = 999999

def dis(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            a = dis(points[i], points[j])
            b = dis(points[j], points[k])
            c = dis(points[i], points[k])
            d = max(a, max(b, c))
            min_d = min(min_d, d)

res = round(math.pi * min_d, 2)
print(res)
