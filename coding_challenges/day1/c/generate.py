import names
import random

MIN_PEOPLE = 10
MAX_PEOPLE = 10

def long_list(people):
    people_str = ""
    if len(people) == 1:
        people_str = people[0]
    elif len(people) == 2:
        people_str = people[0] + " and " + people[1]
    else:
        people_str = ', '.join(people[:-1])
        people_str += " and " + people[-1]
    return people_str

def num(people, single, multiple):
    postfix = single if len(people) == 1 else multiple
    return str(len(people)) + " " + postfix

def hybrid(people):
    people_str = people[0]
    if len(people) > 1:
        people_str += " and " + num(people[1:], "other", "others")
    return people_str

def enter1(people):
    return long_list(people) + " entered the room"

def enter2(people):
    return num(people, "person", "people") + " walked in"

def enter3(people):
    return hybrid(people) + " arrived"

def exit1(people):
    return long_list(people) + " exited the room"

def exit2(people):
    return num(people, "person", "people") + " walked out"

def exit3(people):
    return hybrid(people) + " departed"

enters = [enter1, enter2, enter3]
exits = [exit1, exit2, exit3]

people = set()

for i in range(random.randint(MIN_PEOPLE, MAX_PEOPLE)):
    people.add((names.get_first_name(), False))

actions = []

while people:
    r = random.randint(0, len(people) - 1)
    curr = list(people)[r]

    if not curr[1]:
        actions.append(curr)
        people.remove(curr)
        people.add((curr[0], not curr[1]))
    else:
        actions.append(curr)
        people.remove(curr)
        if (random.randint(0, 1) == 0 and len(people) > 5):
            people.add((curr[0], not curr[1]))


def group_action(group, direction):
    if not direction:
        enter_msg = enters[random.randint(0, len(enters) - 1)]
        return enter_msg(group)
    else:
        exit_msg = exits[random.randint(0, len(exits) - 1)]
        return exit_msg(group)

lines = []

direction = False
group = []
for action in actions:
    # group similar directions
    if action[1] == direction:
        group.append(action[0])
        continue

    # print previous group after direction change
    lines.append(group_action(group, direction))

    # create new group
    group = [action[0]]
    direction = action[1]

lines.append(group_action(group, direction))

print(len(lines))
for line in lines:
    print(line)


