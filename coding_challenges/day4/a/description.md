# Day 4 - Next-Gen Computer - Part A

A new breakthrough technology just got unveiled, the MIYAGI+

It's a computer that is far more advanced than any computer we've seen before.

Its memory has two changes:
1) It can store ternary numbers (base 3) instead of the typical binary numbers (base 2)
2) Memory is stored in 2D instead of the typical 1D 

the MIYAGI+ can have instructions that are made up of 2D areas.

The designers of the MIYAGI+ also made a sylistic choice to use `.`, `!`, and
`#` instead of the normal `0` and `1`.

You've been tasked with analyzing a program written for the MIYAGI+ and find
out how many times a given instruction occurs.

# Input
The first line contains two integers, `iw` and `ih`, which is the width and
height of the instruction you need to count.

The following `ih` lines contain the instruction

The next two integers `pw` and `ph`, are the width and height of the memory for
the program.

The following `ph` lines contain the program

# Output

The number of times that the instruction occurs in the program

# Constraints

`iw = 4`
`ih = 2`
`pw = 2000`
`ph = 1000`

# Examples

Input
```
4 2
.##!
!!..
40 20
.!#!!#!.###.#...!#.###......!###..!!!#!!
###.#!.#.!..!!!!!##!!!#..#!..!...!..!.##
#!#!.#.#!#!#!##!.!##!.###..#!.#.!#!!..#.
.!..#.##!!#..#.!!!!.##!!#.!#!!#.!#!#!###
!!..!!!..##!.!..!....###!#!##..!###.!..#
.!.#.!#!..!...##!#!#.##!#.!#..#!...!....
.!!!#!..!.!!!!#.#...!.!#!###!.##..!###..
#.!..!#!!##..!#.#####..!!!#!#!!..##!..#.
##..!...!.#.!.!.#!..!!#!.#!...!.!#.#.!.!
!!!...#!.!.##..!.##!!#..!!!#!.!.#.!.##..
.!#.#.#.#..!#!.!##.!..#!#...##!!##.!.!##
##!!!.!!!##.#..##......##.#!##..!##.!.!#
!.#.#.#!.##!..##!!!.!###...##!.!!..!!.!#
!!..!#!!#...!!!..#!.!!!#...#!#!#.##..!.!
..#!!.!#!!.!#.#!!..#####!#.##!!!!...!...
..!##!#!!.!#!!...!##!!!!.###.!#!..#..!!!
#!.!#.##!.!..!...#!!!!###!!!#!!#!#!!!#.!
!!..##!#!!##!#!..#...##.!!!.!!#.!.###!##
.!!!!..#.!#.!.#!.#!!#!.!.!#!#.#!.##.##.!
#!..!..#!..#.!!#.!#!..!###..!..!##!##!##
```

Expected Output
```
3
```

Input
```
4 2
#..!
####
40 20
.##.!!#!!...##....!...##!...##.!.#.##..!
!##.!#!.!!..##!.#!#.!###!!##.!.!#!.#!#.!
#!......#!#!##!.!!!##.#.!!!#..!#.#!.##!!
.!.!.###.!!##.#.#!..!...!...##..!#!!.##.
#!#.!.!!..#!.!..##...##!#!#.!!#!##.#.!.#
!!##!##!#!...#!##!#!##.#!.!##..!!!.!.#..
!!.!!#!.!..!.###!######!.#!#!!#.##..!##!
!!.##.!..!.!!!!#.!##!!!..#.!#....!#..!!!
!!..!#!.!!###!!.!.#.!#!##!##!.#!!#.##.!#
#!!!..#!#.#!!!...!#..#!#.#..!....!.!#!!!
#.#...!#!!##.##.#!#!!##..##!.##!#!.##!#.
..###!##!..#!.#!.#!.!#...!#!.!!##.#.#!.!
#..!#!!.!#.#!.!.!..#..!.!###!.!#!##!.!.!
!###.#.#.!#!#!#.!!##.##!.!#..#!!!!####.!
!!#!#!...#......###!!.#!..!#.#!.!!!..!#.
!.#!!!.#!!##!.#.!.!.###!!!#!!!..!#......
!.##..!#!!#.!.#..#####.#.#.##.!!#..###.!
#.#####.#......!!.#!#.!!.#.#.#!.!.!.#!!.
!##!#!#!....!..##!...#..#.!!.##.!#!.####
#!#!#.#..!.!#!.!.!!##.!!#..#...!#!!..!..
```

Expected Output
```
1
```

