import sys
import re

lines = [line.rstrip() for line in sys.stdin.readlines()][1:]
current, most = 0, 0

walked = lambda line: current + int(line[: line.index(" ")])
entered = lambda line: sum([x.isupper() for x in line])
closures = {
    ("entered", "arrived"): entered,
    ("exited", "departed"): lambda l: -1 * entered(l),
}

for line in lines:
    if "walked in" in line:
        current += int(line[: line.index(" ")])
    elif "walked out" in line:
        current -= int(line[: line.index(" ")])
    elif " other" in line:
        num = int(re.findall(r"\d+", line)[0])
        current += (num + 1) if "arrived" in line else -1 * (num + 1)
    else:
        for keylist, closure in closures.items():
            for key in keylist:
                if key not in line:
                    continue
                result = closure(line)
                current += closure(line)
    most = max(most, current)

print(most)
