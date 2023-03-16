kc, kr = [int(x) for x in input().split()]
kernel = [input().rstrip() for _ in range(2)]

bc, br = [int(x) for x in input().split()]

body = []

for _ in range(br):
    body.append(input().rstrip())

def check(r, c):
    global kernel, body
    for rd in range(kr):
        for cd in range(kc):
            # print(rd, cd, r, c)
            if kernel[rd][cd] != body[r+rd][c+cd]:
                return False
    return True

count = 0
for r in range(br-kr+1):
    for c in range(bc-kc+1):
        if check(r, c) == True:
            count += 1

print(count)
