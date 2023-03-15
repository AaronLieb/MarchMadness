import random
import sys
import random
import re

DEBUG = False

MAX_WAIT = 180

MIN_LINES = 100
MAX_LINES = 100

if DEBUG:
    MIN_LINES = 4
    MAX_LINES = 4

sys.setrecursionlimit(max(1000, MAX_LINES + 100))

def time_str(time):
    return str(time//60).zfill(2) + ":" + str(time%60).zfill(2)

def bfs(graph, start, end):
    Q = [start]
    visited = set()
    while Q:
        city = Q.pop()
        if city in visited:
            continue
        visited.add(city)
        for child in graph.nodes[city]:
            if child[1] > MAX_WAIT:
                continue
            if child[0] == end:
                return True
            Q.insert(0, child[0])
    return False

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        self.nodes[name] = []

    def add_flight(self, before, after, wait, duration):
        self.nodes[before].append((after, wait, duration))

n = random.randint(MIN_LINES, MAX_LINES)

with open("../cities.txt", "r") as cities_file:
    lines = [line.rstrip() for line in cities_file.readlines()]

cities = []
for line in lines:
    if len(re.findall(r"\W", line)):
        continue

    cities.append(line.replace(" ", "_").rstrip())

random.shuffle(cities)
cities = cities[:n]

if "Lisbon" not in cities:
    cities.append("Lisbon")
cities_bank = cities[::]

start_city = "Lisbon"
r_idx = random.randint(0, len(cities) - 1)
final_city = cities[r_idx]
while final_city == start_city:
    r_idx = random.randint(0, len(cities) - 1)
    final_city = cities[r_idx]

def generate_graph():
    graph = Graph()

    for city in cities:
        graph.add_node(city)

    flights = []

    for i in range(len(cities) * 5):
        r_idx = random.randint(0, len(cities) - 1)
        before = cities[r_idx]
        r_idx = random.randint(0, len(cities) - 1)
        after = cities[r_idx]
        while before == after:
            r_idx = random.randint(0, len(cities) - 1)
            after = cities[r_idx]

        wait = random.randint(0, 60 * 10)
        duration = random.randint(0, 60 * 5)
        graph.add_flight(before, after, wait, duration)
        flights.append((before, after, wait, duration))

    return flights, graph

flights = None
graph = None
has_path = False
while True:
    flights, graph = generate_graph()
    has_path = bfs(graph, start_city, final_city)
    if has_path:
        break

random.shuffle(flights)

print(start_city)
print(final_city)
print(len(flights))
for flight in flights:
    print(flight[0], flight[1], time_str(flight[2]), time_str(flight[3]))
