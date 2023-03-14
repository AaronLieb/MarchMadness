import re

num = input()
pi = input()

def find(string, thing):
    return len(re.findall(thing, string))

print(find(pi, find(pi, num))

