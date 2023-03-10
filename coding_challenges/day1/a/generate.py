import names
import random

MIN_PEOPLE = 10000
MAX_PEOPLE = 20000

people = set()

for i in range(random.randint(MIN_PEOPLE, MAX_PEOPLE)):
    people.add((names.get_first_name(), False))

actions = []

while people:
    r = random.randint(0, len(people) - 1)
    curr = list(people)[r]

    if not curr[1]:
        actions.append((curr[0], "entered the room"))
        people.remove(curr)
        people.add((curr[0], not curr[1]))
    else:
        actions.append((curr[0], "left the room"))
        people.remove(curr)
        if (random.randint(0, 1) == 0 and len(people) > 5):
            people.add((curr[0], not curr[1]))

print(len(actions))

for action in actions:
    print(action[0], action[1])



