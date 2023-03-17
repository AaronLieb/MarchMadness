# Day 5 - Taxable Income - Part B

The Irrational Relativity Sanction (IRS) wants to calculate the taxable income
for multiple suspicious bank accounts. They have tasked your team, the best in
the Relativity Sanction-ing business, to help find the bank account that made
the most taxable income.

However, due to the Synchronized Integer Enumeration and Validation Exclamation (S.I.E.V.E),
the Irrational Relativity Sanction can only (legally) consider non-prime numbers as taxable income.

There is a wrinkle, though. The IRS stores bank accounts using a `g-Nacci` notation described below.

`g-Nacci`:

`g-Nacci[i]` = `g-Nacci[i-1] + p-Nacci[i-2] + p-Nacci[i-3] + ... + p-Nacci[i-p]`

The first p-Nacci number is always `0` which is then followed by `g-1` `1`'s.

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

`2-Nacci[10] = 37`

`6-Nacci[201] = 1840791`

`7-Nacci[1999] = 2807708`

The final output of a `g-Nacci` sequence at a given index `i` is known as a
`routing number`, as per the IRS's manuals, of course.

## Input

The first line contains two integers `n` and `k`

`n` is the number of bank accounts

`k` is the number of transactions from one `routing number` to another

Each of the next `n` lines contains a bank account. Each bank account consists
of two numbers, the first being the base `g` of the `g-Nacci` sequence. The
next number is the index within that sequence. For example `7 1999` should yield
a final `routing number` of `2807708`

Each of the next `k` lines contains a transaction. A transaction contains 3
numbers. The first being the `routing number` from which money is exiting and
the second being the `routing number` to which money is entering. The final
number, which is surrounded by parenthesis and preceded by a `$`, is the amount
of money transfered.

## Output

The original bank account which can be found by concatenating the base `g` and
the index `i` with no spaces. e.g: `7 1999` -> `71999`

*Note: the transactions show transfers between routing numbers but your output
should be the original bank account.*

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
```

Expected Output
```
```

Input
```
```

Expected Output
```
```
