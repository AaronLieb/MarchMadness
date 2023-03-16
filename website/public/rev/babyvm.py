import sys

mem = ["0"] * 64
memCounter = 0
x = ["0"] * 64
y = ["0"] * 64
z = []
ic = 0

inp = sys.stdin.read(1)
while (inp != '0'):
    if inp == "1":
        memCounter += 1
        mem[memCounter] = 33
    if inp == "2":
        z = x
        x = y
        y = z
    if inp == "3":
        y[memCounter] = mem[memCounter]       
    if inp == "4":
        temp = sys.stdin.read(1)
        print(temp)
        mem[memCounter] = temp
    if inp == "5":
        memCounter -= 1
    inp = sys.stdin.read(1)
    ic += 1
if "GOOD" in "".join(x) and "JOB" in "".join(y):
    if ic % 2 != 0:
        print("almost")
        exit()
    print(open("flag.txt").read())
else:
    print("no lol")
