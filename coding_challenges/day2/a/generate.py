from random import randint

digits = open("./digits.pi").readline()

for x in range(0, 100):
    out = open(f"inputs/{x}.in", "w")
    our_pi = digits[: randint(777, 3141)]
    rint = randint(100, 999)
    out.writelines(str(rint) + "\n")
    out.writelines(our_pi)
