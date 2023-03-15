start = input()
end = input()
n = int(input())

MAX_WAIT = 180

min_time = 999999

def bfs(graph, start, end):
    global min_time
    Q = [(start, 0, [start])]
    while Q:
        curr = Q.pop()
        if curr[0] == end:
            min_time = min(curr[1], min_time)
            return curr
        for child in graph.nodes[curr[0]]:
            if child[1] > MAX_WAIT:
                continue
            Q.insert(0, (child[0], curr[1] + child[1] + child[2], curr[2] + [child[0]]))
    return

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        if name in self.nodes:
            return
        self.nodes[name] = []

    def add_flight(self, before, after, wait, duration):
        if before == after:
            return
        self.nodes[before].append((after, wait, duration))

graph = Graph()

for i in range(n):
    words = input().split()
    before = words[0]
    after = words[1]
    wait = words[2]
    wait = int(wait[:2])*60 + int(wait[3:])
    duration = words[3]
    duration = int(duration[:2])*60 + int(duration[3:])

    graph.add_node(before)
    graph.add_node(after)
    graph.add_flight(before, after, wait, duration)
    
bfs(graph, start, end)

print(min_time)

