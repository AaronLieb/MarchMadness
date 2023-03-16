import sys

def f(x, y):
    if x % 2 != 0:
        return x
    y[0] += 1
    return int(f(x/2, y))

def main():
    a, b, c, d, e = 0, [0], 24, 6, 0
    d, c = c - d, c - d
    input_str = input("Enter a number from 1 to 99999:\n").strip()
    try:
        e = int(input_str)
    except ValueError:
        print("Invalid input.")
        sys.exit(1)

    if e > 0:
        a = f(e, b)
    if b[0] == 7 and (a + b[0]) == c:
        with open("flag.txt") as fp:
            buff = fp.readline().strip()
            print(buff)
    else:
        print("Try again!")

if __name__ == "__main__":
    main()
