import sys

lines = [line.rstrip() for line in sys.stdin.readlines()][1:]


current = 0
most = 0
for line in lines:
    name = line[: line.index(" ")]
    entered = "entered" in line
    current += 1 if entered else -1
    assert current >= 0, "Negative room capacity!"
    most = max(most, current)

print(most)
