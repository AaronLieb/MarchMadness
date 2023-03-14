# Day 2 - π and pie  - Part B

A hiring agency is looking for the most precise engineers and wants to know
which engineers to hire.

Thankfully, there was a recent baking contest for engineers. Each engineer was
tasked with baking a pie of a specified radius.

The engineers suck at baking and all of their pies turned out perfectly flat.
Since the top of the pie is always completely flat, the engineers needed to
know the area of the top of the pie to determine how much dough they needed to
cover the top of the pie completely with crust.

Baking pans were provided to the engineers that guaranteed that the pie is the
specified radius. While calculating the area, many of the engineers used
approximations for π that were "close enough". 

The hiring agency holds the strong belief that the value of π used should
always be at least 15 decimal places. Here is the value of π to the 15th
decimal place (you should use this value as your "real" value of π):

π = `3.141592653589793`

## Input
The first line contains an integer `n`, the number of engineers.

The next `n` following lines contain an integer `r` and a decimal `a`.

`r` is the radius of the pie, and `a` is the area of the top of the pie that the
engineer estimated.

## Output

The hiring agency is interested in the engineers that used the most accurate
value of π. 

For each engineer, you should determine what approximate value of
π they used to calculate the area. 

Each engineer's "error" is the difference between their approximate value of π
and the "real" value of π. 

Output one integer, the product of the radii given to the 5 engineers with the
lowest error.

## Constraints
`10000 <= n <= 20000`

`1 <= r <= 20`

## Examples

