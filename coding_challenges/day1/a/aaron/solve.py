def solve():
    n = int(input())

    in_room = set()

    max_ppl = 0
    for i in range(n):
        words = input().split()
        if words[1] == "entered":
            max_ppl = max(max_ppl, len(in_room))
            in_room.add(words[0])
        else:
            in_room.remove(words[0])

    print(max_ppl)

if __name__ == "__main__":
    solve()

