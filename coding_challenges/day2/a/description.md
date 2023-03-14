# Day 2 - Patterns in π - Part A

Happy Pi Day! Your physics professor, Professor Pippy wanted to do a fun
pi-related problem. 

Here's the challenge: 

Write a program that takes in two inputs.

The first input is a string that represents the decimal expansion of Pi. 
The second input is a three-digit integer `d`

1. Count the number of times the three-digit integer `d` occurs in
the Pi string `c`

2. Then count the number of times that `c` occurs in
the Pi string. 

Unfortunately, professor Pippy had to leave for a dentist appointment
scheduled at 3:14pm!

Help professor Pippy solve this problem and you might just get an A in the class!


## Input
A string S representing the decimal expansion of Pi
A three-digit integer N (for example, 123, 456, or 789)

## Output

The number of times that `c` appears in the given pi string.

## Constraints
`100 <= d <= 999`
`777 <= pi string length <= 3141`

## Examples

Input
```
749
3.1415926535897932384626433832795028841971693993751058209749445
```

Expected output
```
5
```

Input
```
360
3.1415965358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160
```

Expected output
```
44
```



