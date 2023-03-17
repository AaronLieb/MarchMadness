from util import kNacci
import sys

lines = [line.rstrip() for line in sys.stdin.readlines()]

for line in lines:
    p, i = [int(x) for x in line.split()]
    print(kNacci(p, i))
