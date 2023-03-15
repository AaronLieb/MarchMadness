from collections import defaultdict

start = input().rstrip()
end = input().rstrip()
n = int(input())

G = defaultdict(lambda: list())
kMAX_WAIT = 180  # 3 hours -> 180 minutes


def toMinutes(t: str) -> int:
    hours = int(t[:2])
    minutes = int(t[3:])
    return minutes + hours * 60


for _ in range(n):
    u, v, wait, dur = [x.rstrip() for x in input().split()]
    wait = toMinutes(wait)
    dur = toMinutes(dur)
    G[u].append((v, wait, dur))


# now bfs
best = 10**18
visited = set()
Q = [("Lisbon", 0)]
while len(Q):
    city, time = Q.pop(0)

    if city == end:  # arrived
        best = min(best, time)

    # append neighbors
    for next in G[city]:
        name, wait, dur = next
        if wait > kMAX_WAIT or name in visited:
            continue
        visited.add(name)
        Q.append((name, time + dur + wait))

print(best)
