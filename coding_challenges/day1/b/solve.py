def solve():
    n = int(input())

    in_room = 0

    ignore_list = ["the", "and", "person", "people", "other", "others", "walked", "room"]
    enter_list = ["arrived", "entered", "in"]

    max_ppl = 0
    for i in range(n):
        words = input().split()
        words = list(filter (lambda w: w not in ignore_list, words))
        num = len(words) - 1
        dir = words[-1]

        if words[-2].isnumeric():
            num += int(words[-2]) - 1

        if dir in enter_list:
            in_room += num
            max_ppl = max(max_ppl, in_room)
        else:
            in_room -= num

    print(max_ppl)

if __name__ == "__main__":
    solve()

