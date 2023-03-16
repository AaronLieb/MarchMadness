from random import randint

one = """

   |
   |

"""
two = """
  __
  _|
 |_

"""
s = [
    "        __   _         _    _   _    _    _    _   ",
    "   |    _|   _|  |_|  |_   |_    |  |_|  |_|  | |  ",
    "   |   |_    _|    |   _|  |_|   |  |_|   _|  |_|  ",
    "                                                  ",
]

line = [["x"] * 47 for _ in range(4)]


def genNum(n):
    two_digit = False
    if n >= 10:
        two_digit = True
    l = line[::]
    # 4 rows, 3 cols
    sc = 1
    for _ in range(n):
        k = randint(0, 9)
        tl = k * 4 + 1
        for i in range(4):
            for j in range(3):
                l[i][j + sc] = s[i][j + tl]
        sc += 3
        #     out += s[i][j + tl]
        # out += "\n"
    return l


n = genNum(2)
for row in n:
    print("".join(row))
# print(genNum(0))


# nums = {k: getNum(k) for k in range(10)}

# print(nums)
# print(nums[0], end="")
# print(nums[1])

# for _ in range(20):
#     ridx = randint(0, 9)
#     print(nums[ridx], end="")
