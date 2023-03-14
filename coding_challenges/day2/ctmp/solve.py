n = int(input())

PI = 3.141592653589793

points = []
for _ in range(n):
    x, y = [int(i) for i in input().split()]
    points.add((x, y))


def dist(p1, p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(.5)

def middle(p1, p2, p2):
    # get average of all x's and y's
    n = 3
    cx = p1[0] + p2[0] + p3[0]
    cy = p1[1] + p2[1] + p3[1]
    return (cx / n, cy / n)

def circumference(r):
    return PI * r * 2

dists = []
smallest = 10**18
for p1 in points:
    for p2 in points:
        if p1 == p2: continue # dont use same
        for p3 in points:
            if p3 == p2 or p3 == p1: continue
            mid = middle(p1, p2, p3)
            # check furthest point from middle is radius
            radius = max(dist(mid, p1), dist(mid, p2), dist(mid, p3))
            smallest = min(smallest, circumference(radius))

print(smallest)


# get all possible permk
