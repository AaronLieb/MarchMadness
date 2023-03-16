import random

DEBUG = False

BOARD_SIZE = 2000
FIND_SIZE = 4

if DEBUG:
    BOARD_SIZE = 40

chars = ".!#"

print(FIND_SIZE, FIND_SIZE//2)
for row in range(FIND_SIZE//2):
    for col in range(FIND_SIZE):
        r = random.randint(0, len(chars) - 1)
        print(chars[r], end='')
    print()

print(BOARD_SIZE, BOARD_SIZE//2)
for row in range(BOARD_SIZE//2):
    for col in range(BOARD_SIZE):
        r = random.randint(0, len(chars) - 1)
        print(chars[r], end='')
    print()

        
