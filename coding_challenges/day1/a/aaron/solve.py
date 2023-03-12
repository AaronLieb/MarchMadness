def solve():
    n = int(input())

    in_room = 0
    max_ppl = 0
    for i in range(n):
        words = input().split()
        if words[1] == "entered":
            in_room += 1
            max_ppl = max(max_ppl, in_room)
        else:
            in_room -= 1

    print(max_ppl)

if __name__ == "__main__":
    solve()

