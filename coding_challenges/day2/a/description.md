# Day 2 - Patterns in π - Part A


It's Pi day and your physics professor is giving the class an extra credit
assignment.

Write a program that takes two inputs: a string representing the decimal
expansion of Pi (up to at least 1000 decimal places), and a three-digit
integer. The program should first count the number of times the three-digit
integer occurs in the Pi string, and then count the number of times that count
occurs in the Pi string as well. Return the final count as the output.

## Input
A string S representing the decimal expansion of Pi
A three-digit integer N (e.g. 123, 456, 789)

## Output

## Constraints

## Examples

# Day 2 - Pi Pursuit - Part B

Engineers are calculating the area of circles

each engineer uses their own approximate of pi that is "close enough"

A hiring agency is looking for the most precise engineers, and wants to know what which engineers hire.

Thankfully, there was a recent baking contest for engineers.

Each engineer was tasked with baking a pie of a specified radius. 

Each engineer needed to know how much pie crust to put on the top, so they each calculated the area of the top of the pie.

Engineers are pretty bad bakers, so the top of the pie is always completely flat.
Baking pans were provided to the engineers that guarantee that the pie is the specified radius

They needed to know the area of the top of the pie so that they know how much
dough they needed to cover the top of the pie completely with crust.

While calculating the area, many of the engineers used approximations for pie that were "close enough".
The hiring agency is interested in finding out who the most precise engineers were at the competition!

The hiring agency holds the strong belief that the value of pi used should always be at least 15 decimal places.
Here is the value of pi to the 15th decimal place (you should use this value as your "real" value of pi):

`3.141592653589793`


## Input

The first line contains an integer `n`, the number of engineers
The next `n` following lines contain an integer `r`, and decimal `a`.
`r` is the radius of the pie
`a` is the area of the top of the pie that the engineer estimated.

## Output

The hiring agency is interested in the engineers that used the most accurate value of pi.
For each engineer, you should determine what approximate value of pi they used to calculate the area.
Each engineers "error" is the difference between their approximate value of pi, and the "real" value of pi
Each engineer is graded on how close they were to the "real" value of pi
Output one integer, the product of the radii given to the top 5 most precise engineers

## Constraints

## Examples

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



