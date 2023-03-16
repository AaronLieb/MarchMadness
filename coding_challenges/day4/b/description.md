# Day 4 - Seven Pain Display: A Parsing Nightmare - Part B

MIYAGI+ is more advanced than we initially thought. Scientists aren't quite
sure what MIYAGI+'s potential really is, though.

Your team has been tasked with assisting MIYAGI+ researchers with a *simple*
task.

MIYAGI+ is known to be a fast calculator of simple math equations, but just how
accurate is MIYAGI+? The researchers have decided to test MIYAGI+'s accuracy by
giving it math equations to solve. Of course, MIYAGI+'s input is a 2D matrix of
`.` `!` and `#` which isn't very human readable. Therefore, the kind
researchers have prepared a special handwritten version of the input just for
you. Since MIYAGI+'s Load Memory Alignment Overload (LMAO) is still a work in
progress, the researchers request that you modulo each equation's result by
`10^7` so they can compare your results to MIYAGI+'s.

# Input
The first line of input `n` contains the number of math equations to follow.

Each of the next `n` lines contains a simple math equation consiting of
integers, floating point numbers, and operators. The operators consist of `+`,
`-` and `*`.

# Output

The final sum of the results of each equation **rounded** to two decimal places.

*Modulo each equation's result by `10^7`*

*Note: using the modulo operator on a negative number produces a positive
number, account for this.*

# Constraints

`1000 <= n <= 2000`

Each integer and floating point number are `>= 1` and `<= 99999`.

*Note: a `-` operator in front of a number essentially swaps its domain to `<= -1` and `>= -99999`

# Examples

Input
```
4
###  ###       ###  ###  ###  ###       ###  ###  ###  ###
# #  # #       # #    #  # #    #   #   # #    #  # #  # #
###  ###  ###  ###    #  # #    #  ###  ###    #  ###  ###
# #    #       # #    #  # #    #   #     #    #  # #    #
###  ###       ###    #  ###    #       ###    #  ###  ###

###       ###  ###       ###
  #   #     #  #     #   # #
  #  ###  ###  ###  ###  ###
  #   #     #    #   #     #
  #       ###  ###       ###

###  ###  ###       ###  ###       ###  ###  ###  ###
# #  # #  # #   #   # #  # #       #      #  #    # #
###  ###  ###  ###  ###  ###  ###  ###  ###  ###  # #
  #  # #    #   #   # #  # #       # #  #    # #  # #
###  ###  ###       ###  ###       ###  ###  ###  ###

# #       ###  ###       ###  ###
# #   #     #    #         #    #
###  ###    #  ###  ###  ###  ###
  #   #     #    #         #    #
  #         #  ###       ###  ###

```

Expected Output
```
9996083.00
```

Explanation
```
89-8707+9789 = 1171
sum = 0 + 1171 = 1171
sum %= 10**7  =  1171

7+35+9 = 51
sum = 1171 + 51 = 1222
sum %= 10**7  =  1222

989+88-6260 = -5183
sum = 1222 + -5183 = -3961
sum %= 10**7  =  9996039

4+73-33 = 44
sum = 9996039 + 44 = 9996083
sum %= 10**7  =  9996083
```

Input
```
7
###  ###       ###  ###       ###  ###  ###
# #    #       # #  # #       # #    #  #
###  ###  ###  ###  ###  ###  ###  ###  ###
# #    #       # #  # #       # #    #  # #
###  ###       ###  ###       ###  ###  ###

###  ###       ###       #  ###       ###  ###  ###  ###
  #    #   #   #         #  # #   #   #    # #    #    #
###  ###  ###  ###       #  ###  ###  ###  ###  ###    #
  #    #   #   # #       #  # #   #   # #    #    #    #
###  ###       ###   #   #  ###       ###  ###  ###    #

###  # #  ###        #   #  ###  ###        #   #  ###
#    # #  # #   #    #   #    #  #          #   #  # #
###  ###  ###  ###   #   #  ###  ###  ###   #   #  # #
# #    #    #   #    #   #    #  # #        #   #  # #
###    #  ###        #   #  ###  ###        #   #  ###

###       # #  ###  ###       ###  ###
  #       # #  # #  #     #     #  #
###  ###  ###  # #  ###  ###    #  ###
#           #  # #  # #   #     #    #
###         #  ###  ###         #  ###

###  ###  ###  ###       ###  ###       ###      ###  ###  ###  # #
# #  # #  # #    #         #    #   #   #        #    #    #    # #
###  # #  ###    #  ###    #    #  ###  ###      ###  ###  ###  ###
# #  # #    #    #         #    #   #   # #        #  # #  # #    #
###  ###  ###    #         #    #       ###   #  ###  ###  ###    #

###  ###  ###  ###       ###       ###  ###
  #  # #    #  # #         #         #  #
###  ###  ###  # #  ###  ###  ###    #  ###
  #    #    #  # #         #         #    #
###  ###  ###  ###       ###         #  ###

 #  ###       ###  ###  ###       ###      ###  ###  ###
 #    #       #    # #  # #   #     #      #      #  # #
 #  ###  ###  ###  ###  ###  ###  ###      ###  ###  # #
 #  #         # #    #  # #   #   #        # #    #  # #
 #  ###       ###  ###  ###       ###   #  ###  ###  ###

```

Expected Output
```
18676.38
```

Explanation
```
83-88-836 = -841
sum = 0 + -841 = -841
sum %= 10**7  =  9999159
33+6.18+6937 = 6976.18
sum = 9999159 + 6976.18 = 10006135.18
sum %= 10**7  =  6135.18
649+1136-110 = 1675
sum = 6135.18 + 1675 = 7810.18
sum %= 10**7  =  7810.18
2-406+75 = -329
sum = 7810.18 + -329 = 7481.18
sum %= 10**7  =  7481.18
8097-77+6.5664 = 8026.57
sum = 7481.18 + 8026.57 = 15507.75
sum %= 10**7  =  15507.75
3930-3-75 = 3852
sum = 15507.75 + 3852 = 19359.75
sum %= 10**7  =  19359.75
12-698+2.630 = -683.37
sum = 19359.75 + -683.37 = 18676.38
sum %= 10**7  =  18676.38
```
