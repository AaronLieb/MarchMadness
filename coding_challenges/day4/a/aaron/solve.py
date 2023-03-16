lw, lh = [int(x) for x in input().split()]
lookup = []
for row in range(lh):
    lookup.append(input())

bw, bh = [int(x) for x in input().split()]
board = ""
for row in range(bh):
    board += input()

sum = 0
for i in range(len(board) - bw - lw):
    good = True
    for row_offset in range(len(lookup)):
        for col_offset in range(len(lookup[row_offset])):
            board_offset = i + (row_offset * bw) + col_offset
            if board[board_offset] != lookup[row_offset][col_offset]:
                good = False
    if good:
        sum += 1

print(sum)
            
