# Day 5 - Taxable Income - Part B

The Irrational Relativity Sanction (IRS) wants to calculate the taxable income
for multiple suspicious bank accounts. They have tasked your team, the best in
the Relativity Sanction-ing business, to help find the bank account that made
the most taxable income.

However, due to the Synchronized Integer Enumeration and Validation Exclamation (S.I.E.V.E),
the Irrational Relativity Sanction can only (legally) consider non-prime numbers as taxable income.

There is a wrinkle, though. The IRS stores bank accounts using a `p-Nacci` notation described below.

`p-Nacci`:

`p-Nacci[i]` = `p-Nacci[i-1] + p-Nacci[i-2] + p-Nacci[i-3] + ... + p-Nacci[i-p]`

The first p-Nacci number is always `0` which is then followed by `p-1` `1`'s.

** For example: **
*for `p` = 3*

Our starting sequence for `3-Nacci` is `[0, 1, 1]`

Calculating the next `3-Nacci` number requires finding the sum of the previous `3`.

i.e: `0 + 1 + 1 = 2`. Therefore `3-Nacci[4] = 2`.

Moreover, `3-Nacci[5] = 4`, `3-Nacci[6] = 7` ... `3-Nacci[12] = 274`.

There's more. Due to government budget cuts, the IRS also has an extremely
primitive computational network called the Unrelenting Homogenous-Oxidation Hole (Uh-Oh).
Due to this, the IRS requests that when calculating `p-Nacci` numbers you should
also modulo each of the `p` previous values by `10**7+7` as well as the final
result for a given index.

Below are some examples the IRS gave you to help calibrate your work:

`2-Nacci[10] = 37`

`6-Nacci[201] = 1840791`

`7-Nacci[1999] = 2807708`

## Input

The first line contains two integers `n` and `k`.

`n` is the number of bank accounts.

`k` is the number of transactions from one bank account to another

Each of the next `n` lines contains a bank account. Each bank account consists
of two numbers, the first being the base `p` of the `p-Nacci` sequence. The
next number is the index within that sequence. For example `7 1999` should yield
a final `routing number` of `2807708`

## Output

An integer (no commas or $) representing the amount in dollars that Charlie
will have to pay in taxes rounded to the nearest whole number

## Constraints

`b = 50`
`10000 <= n <= 20000`

## Examples

Input
```
8
22
$12,622 $32,448 0%
$32,449 $59,824 23%
$59,825 $163,573 37%
$163,574 $267,261 50%
$267,262 $594,868 61%
$594,869 $1,426,679 71%
$1,426,680 $2,162,839 81%
$2,162,840 $5,293,352 91%
$11,122
$8,738
$9,960
$16,697
$3,474
$252
$14,075
$8,841
$1,399
$15,164
$5,382
$1,968
$20,525
$14,570
$23,314
$4,314
$7,993
$4,571
$4,696
$1,325
$4,340
$1,257
```

Expected Output
```
71110
```

Input
```
8
22
$10,570 $28,702 0%
$28,703 $54,727 23%
$54,728 $141,877 37%
$141,878 $396,507 50%
$396,508 $1,162,531 61%
$1,162,532 $1,952,933 71%
$1,952,934 $3,307,595 81%
$3,307,596 $8,421,204 91%
$14,204
$14,933
$2,481
$9,102
$135
$10,675
$3,282
$10,860
$22,868
$9,655
$4,918
$3,311
$10,251
$10,558
$10,862
$3,903
$5,288
$981
$8,118
$7,921
$698
$4,595
```

Expected Output
```
66444
```
