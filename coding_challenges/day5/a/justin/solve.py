from re import sub

num_brackets = int(input())
num_paychecks = int(input())

brackets = []
for _ in range(num_brackets):
    line = input().rstrip()
    line = sub(r'[$,%]', '', line)
    bmin, bmax, rate = [int(x) for x in line.split()]
    brackets.append((bmin, bmax, rate))

total = 0
for _ in range(num_paychecks):
    line = input().rstrip()
    line = sub(r'[$,]', '', line)
    money = int(line)
    total += money if money > 100 else 0

# now calculate taxes paid
in_taxes = 0.0

# subtract from total anything below first tax bracket
print(total)
print(brackets)
# total -= brackets[0][1]
# print('aft: ', total)
current_bracket = 0
while current_bracket < num_brackets:
    b = brackets[current_bracket]
    l, r, rate = b
    rate /= 100 # 20 -> .2

    if total >= l:
        print('rate: ', rate)
        taxed_ranged = min(total-l, r - l)
        amnt = taxed_ranged * rate
        in_taxes += amnt

    current_bracket += 1

print('Amount of money left over to spend on w33d', total-in_taxes)
print('Paid in taxes', in_taxes)
