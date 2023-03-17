# Day 5 - Tax Brackets - Part A

Tax season is coming up your uncle Charlie Taylor is doing his taxes.

He hates technology and refuses to use any online tools to help him calculate his taxes.
Hes asked if you could help him calculate how much he paid in taxes this year!

Tax brackets work by dividing your income into ranges, and you are only taxed
at the specified rate for the income that falls within each range. Any income
that falls above a certain range is taxed at a higher rate, while income that
falls below a certain range is taxed at a lower rate or not taxed at all.

Charlie has also requested that you don't count any checks that are $100 or less!
The IRS will never find out!

## Input

The first line contains an integer `b`, the number of tax brackets.
The second line contains an integer `n`, the number of paychecks that contribute to Charlie's taxable income.
The following `b` lines each contain two amounts of money `bmin` and `bmax` and a percentage `rate`

Any income in the range of `bmin` and `bmax` will be taxed at `rate`

The following `n` lines each contain an amount of money `m`
This means Charlie received a check of amount `m` that contributes towards his taxable income.

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
