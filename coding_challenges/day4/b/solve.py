import sys
from random import randint, choice

representations = {
    "0": ("###", "# #", "# #", "# #", "###"),
    "1": (" #", " #", " #", " #", " #"),
    "2": ("###", "  #", "###", "#  ", "###"),
    "3": ("###", "  #", "###", "  #", "###"),
    "4": ("# #", "# #", "###", "  #", "  #"),
    "5": ("###", "#  ", "###", "  #", "###"),
    "6": ("###", "#  ", "###", "# #", "###"),
    "7": ("###", "  #", "  #", "  #", "  #"),
    "8": ("###", "# #", "###", "# #", "###"),
    "9": ("###", "# #", "###", "  #", "###"),
    ".": ("  ", "  ", "  ", "  ", " #"),
    "+": ("   ", " # ", "###", " # ", "   "),
    "-": ("   ", "   ", "###", "   ", "   "),
    "*": ("   ", "# #", " # ", "# #", "   "),
}


def seven_segment(number: str):
    digits = [representations[digit] for digit in number]
    for i in range(5):
        print("  ".join(segment[i] for segment in digits))


MAX_EQUATION_LENGTH = 10


def generateEquation():
    symbols = ".+-*"
    nums = "0123456789"
    eq = []
    for _ in range(randint(3, MAX_EQUATION_LENGTH)):
        is_float = randint(0, 10) == 1
        if is_float:
            li = randint(1, 9)
            left = nums[li]
            rights = "".join([choice(nums) for _ in range(randint(1, 4))])
            actual = f"{left}.{rights}"
            eq.append(actual)
            eq.append(choice(symbols[1:]))
            continue
        # not float
        first = choice(nums[1:])  # cant be zero
        # rest
        rest = "".join([choice(nums) for _ in range(randint(0, 4))])
        eq.append(f"{first}{rest}")
        eq.append(choice(symbols[1:]))
    return eq


MAX_LINES = 2000
lines = randint(1000, 2000)
sum = 0
for _ in range(lines):
    ans = "".join([x for x in generateEquation()[:-1]])
    # print(ans)
    result = eval(ans)
    seven_segment(ans)
    print()
    sum += result
    sum %= 10**7

try:
    a = 5 // 0
except ZeroDivisionError as e:
    print(round(sum, 2), file=sys.stderr)
