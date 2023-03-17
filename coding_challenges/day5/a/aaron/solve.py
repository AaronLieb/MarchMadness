b = int(input())
n = int(input())

def read_money(money):
    return int(money.replace(',', '')[1:])

brackets = []
for i in range(b):
    items = input().split()
    min_amt = read_money(items[0])
    max_amt = read_money(items[1])
    percent = float(items[2][:-1])/100
    brackets.append((min_amt, max_amt, percent))

income = 0
for i in range(n):
    money = read_money(input())
    if money > 100:
        income += money

taxes = 0
for i in range(0, len(brackets)):
    min_amt, max_amt, rate = brackets[i]
    diff = max_amt - min_amt
    if income < diff:
        taxes += income * rate
        break
    if income >= diff:
        taxes += diff * rate
        income -= diff

print(round(taxes))

