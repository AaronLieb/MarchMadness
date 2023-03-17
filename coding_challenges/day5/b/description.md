# Day 5 - Taxable Income - Part B

The Irrational Relativity Sanction (IRS) wants to calculate the taxable income
for multiple suspicious bank accounts. They have tasked your team, the best in
the Relativity Sanction-ing business, to help find the bank account that made
the most taxable income.

However, due to the Synchronized Integer Enumeration and Validation Exclamation (S.I.E.V.E),
the Irrational Relativity Sanction can only (legally) consider non-prime numbers as taxable income.

There is a wrinkle, though. The IRS stores bank accounts using a `g-Nacci` notation described below.

`g-Nacci`:

`g-Nacci[i]` = `g-Nacci[i-1] + g-Nacci[i-2] + g-Nacci[i-3] + ... + g-Nacci[i-g]`

The first `g-Nacci` number is always `0` which is then followed by `g-1` `1`'s.

** For example: **
*for `g` = 3*

Our starting sequence for `3-Nacci` is `[0, 1, 1]`

Calculating the next `3-Nacci` number requires finding the sum of the previous `3`.

i.e: `0 + 1 + 1 = 2`. Therefore `3-Nacci[4] = 2`.

Moreover, `3-Nacci[5] = 4`, `3-Nacci[6] = 7` ... `3-Nacci[12] = 274`.

There's more. Due to government budget cuts, the IRS also has an extremely
primitive computational network called the Unrelenting Homogenous-Oxidation Hole (Uh-Oh).
Due to this, the IRS requests that when calculating `g-Nacci` numbers you should
also modulo each of the `g` previous values by `10^7+7` as well as the final
result for a given index.

Below are some examples the IRS gave you to help calibrate your work:

`2-Nacci[10] = 34`

`6-Nacci[201] = 5006161`

`7-Nacci[1999] = 8039002`

The final output of a `g-Nacci` sequence at a given index `i` is known as a
`routing number`, as per the IRS's manuals, of course.

## Input

The first line contains two integers `n` and `k`

`n` is the number of bank accounts

`k` is the number of transactions from one `routing number` to another

Each of the next `n` lines contains a bank account. Each bank account consists
of two numbers, the first being the base `g` of the `g-Nacci` sequence. The
next number is the index within that sequence. For example `7 1999` should yield
a final `routing number` of `8039002`

Each of the next `k` lines contains a transaction. A transaction contains 3
numbers. The first being the `routing number` from which money is exiting and
the second being the `routing number` to which money is entering. The final
number, which is surrounded by parenthesis and preceded by a `$`, is the amount
of money transfered.

## Output

The original bank account whose `routing number` received the most taxable income.

Concatenate the bank account base `p` with its index `i` with no spaces. e.g: `7 1999` -> `71999`

*Note: the transactions show transfers between routing numbers but your output
should be the original bank account associated with the routing number, but not
the routing number itself*

## Constraints

`2000 <= n <= 4000`

`10000 <= k <= 20000`

`2 <= p <= 9`

`100 <= i <= 10000`

`MOD = 10^7+7`

`4 <= transaction amount < MOD`

## Examples

Input
```
3 6
2 6584
9 1802
5 1807
8421011 -> 2801755 ($2716163)
9903020 -> 2801755 ($9594391)
9903020 -> 8421011 ($5769425)
9903020 -> 8421011 ($2078355)
8421011 -> 2801755 ($5577577)
2801755 -> 9903020 ($2249560)
```

Expected Output
```
26584
```

Input
```
8 40
2 5658
9 1408
2 5828
9 1501
2 7924
9 1207
5 3092
3 4560
4296487 -> 2225009 ($8677503)
5354529 -> 5768834 ($3634955)
7488763 -> 5354529 ($704226)
7488763 -> 5768834 ($7545150)
5354529 -> 9234689 ($5302603)
4296487 -> 5768834 ($2896818)
2225009 -> 4296487 ($2202401)
5354529 -> 7488763 ($5281635)
5768834 -> 4296487 ($650471)
8591387 -> 780712 ($8318161)
9234689 -> 780712 ($6699814)
7488763 -> 9234689 ($3025330)
2225009 -> 9234689 ($6786084)
780712 -> 7488763 ($3531843)
4296487 -> 7488763 ($7051813)
4296487 -> 8591387 ($5375510)
2225009 -> 9234689 ($2995702)
5768834 -> 8591387 ($4356904)
5354529 -> 9234689 ($2752475)
4296487 -> 7488763 ($5651415)
9234689 -> 5768834 ($3503021)
9234689 -> 780712 ($3698275)
780712 -> 2225009 ($837580)
4296487 -> 2225009 ($7542725)
8591387 -> 4296487 ($767345)
2225009 -> 7488763 ($2435223)
9234689 -> 7488763 ($5469776)
5354529 -> 7488763 ($9044531)
2225009 -> 4296487 ($4645197)
5768834 -> 8591387 ($5831801)
5768834 -> 8591387 ($1596987)
4296487 -> 9234689 ($2000438)
5768834 -> 8591387 ($5013171)
2225009 -> 5768834 ($6646064)
8591387 -> 7488763 ($4473166)
5768834 -> 2225009 ($5319756)
9234689 -> 780712 ($9266272)
780712 -> 5768834 ($5955033)
4296487 -> 8591387 ($3566529)
780712 -> 5354529 ($9579464)
```

Expected Output
```
53092
```
