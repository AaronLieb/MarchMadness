import sys
board = []
rows = ['a', 'b', 'c', 'd', 'e', 'f']
for i in range(0, len(rows)):
    board.append([' '] * 7)

class Stack:
    def __init__(self):
        self._list = []
    
    def __len__(self):
        return len(self._list)    
    
    def push(self, element):
        if len(self._list) <= 6:
            self._list.append(element)
        else:
            return
    
    def peek(self):
        return self._list[-1]

def initStacks():
    S = [ Stack(), Stack(), Stack(), 
         Stack(), Stack(), Stack(), Stack() ]
    return S

def move(stacks, sum):
    Set0 = {'1', '2', '3', '4', '5', '6', '7'}
    print("Which column?")
    pos = str(sys.stdin.readline().strip())
    if pos not in Set0:
        print("Input must be between 1 and 7")
        move(stacks)
    else:
        pos = int(pos)
        if len(stacks[pos-1]) < 6:
            stacks[pos - 1].push("X")
            sum += 6 - len(stacks[pos-1])
            board[6-len(stacks[pos-1])][pos-1] = stacks[pos-1].peek()
        else:
            print('Column full!')
            move(stacks)
    return stacks, sum

def printBoard():
    rows = ['a','b','c','d','e','f']   
    top = '    1   2   3   4   5   6   7   '
    row = [[n] for n in range(0,7)]
    row[0][0] = 'f | '
    row[1][0] = 'e | '
    row[2][0] = 'd | '
    row[3][0] = 'c | '
    row[4][0] = 'b | '
    row[5][0] = 'a | '
    print('')
    print('  ' + '-'*(len(top)-3))
    for j in range(0,len(rows)):
        for i in range(1,8):
            row[j][0] = row[j][0] + str(board[j][i-1]) + ' | '
        print(row[j][0])
        print('  ' + '-'*((len(row[j][0])-3)))
    print(top)
    print('')

def checkWin(board):
    game = False   

    for j in range(0,6):
        for i in range(3,7):
            if (board[j][i]==board[j][i-1]== board[j][i-2]==board[j][i-3]=="X"):
                    game = True
            else:
                continue   
 
    for i in range(0,7):
        for j in range(3,6):
            if (board[j][i]==board[j-1][i]== board[j-2][i]==board[j-3][i]=="X"):
                    game = True
            else:
                continue

    for i in range(0,4):
        for j in range(0,3):
            if (board[j][i]==board[j+1][i+1]==board[j+2][i+2]==board[j+3][i+3]=="X" or board[j+3][i]==board[j+2][i+1]==board[j+1][i+2]==board[j][i+3]=="X"):
                    game = True
            else:
                continue
    if game:
        print('Game over!')
        if sum == 65:
            flag = open("flag.txt", "r")
            print("Congrats! You actually won! " + flag.read())
            flag.close()
    return game


printBoard()
stacks = initStacks()
sum = 0
game = False
while not game:
    stacks, sum = move(stacks, sum)
    printBoard()
    game = checkWin(board)
