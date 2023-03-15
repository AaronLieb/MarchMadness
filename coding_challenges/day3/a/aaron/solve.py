start = input()
end = input()
n = int(input())

d = dict()
for i in range(n):
    cities = input().split()
    d[cities[0]] = cities[1]

e = 0
curr = start
while(curr != end):
    to = d[curr]
    if len(to) > len(curr):
        e += 5
    elif len(to) < len(curr):
        e -= 2
    curr = to

print(e)



