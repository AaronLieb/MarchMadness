import random
import sys
import random
import re

DEBUG = True

MIN_LINES = 4000
MAX_LINES = 8000

if DEBUG:
    MIN_LINES = 40
    MAX_LINES = 100

sys.setrecursionlimit(max(1000, MAX_LINES + 100))

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

flights = []
max_flights = random.randint(n//6, n//4)
second_run = False
final_city = None

def recur(start_city):
    global second_run
    global final_city
    global flights

    if not cities_bank:
        return

    if len(flights) == max_flights and not second_run:
        final_city = start_city
        second_run = True
    end_city = None
    while end_city == start_city or end_city == None:
        r = random.randint(0, len(cities_bank) - 1)
        end_city = cities_bank[r]
    cities_bank.remove(end_city)
    flights.append((start_city, end_city))
    recur(end_city)

start_city = "Lisbon"
cities_bank.remove(start_city)
recur(start_city)

random.shuffle(flights)

print(start_city)
print(final_city)
print(len(flights))
for flight in flights:
    print(flight[0], flight[1])
