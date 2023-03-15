import sys

lines = [line.rstrip() for line in sys.stdin.readlines()]

start, end = lines[:2]
# print(start, end)
# print(lines)

# create linkings
links = {}
for l in lines[3:]:
    u, v = l.split(" ")
    links[u] = v


# print(links[start])

# follow path

elusive = 0
curr = start
while curr != end:
    if len(links[curr]) > len(curr):
        elusive += 5
    if len(links[curr]) < len(curr):
        elusive -= 2
    curr = links[curr]

print(elusive)
