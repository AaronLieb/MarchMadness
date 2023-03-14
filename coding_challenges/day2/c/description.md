# Day 2 - π and pie  - Part C

Professor Pippy is going to his dentist appointment. He's very concerned that
he might get ripped off by the dentist, so he always consults three differnet
offices.

Professor Pippy is obsessed with optimization and wants to make sure that he finds the three dentist
offices that are closet to eachother.

In order to find out which dentist offices are the closest, he found all
groupings of 3 offices and drew a circle that perfect encompassed all of them.

The smaller the radius of the circle, the closer the dentist offices are.

This is really hard to do by hand, so Professor Pippy has asked if you could
help him locate the 3 dentist offices that are closest together (smallest radius)

## Input

The first line contains an integer `n`, the number of dentist offices

The next `n` following lines contain an integer `x` and a decimal `y`.

## Output

Output the circumference of the smallest circle containing 3 dentist offices.

## Constraints
`n = 20`
`-2000 <= x <= 2000`
`-2000 <= y <= 2000`

## Examples

Input
```
8
17 1114.2337829671942
12 508.4958416468331
16 534.1319285143168
19 1318.540758136722
14 429.68040059057483
16 740.962178105143
18 1015.2554404694425
10 285.5274332392959
```

Expected output
```
656640
```

Input
```
10
12 415.87439964076873
16 677.9721431852045
15 552.1617255431586
20 1017.6519886367032
10 257.1309252497689
13 510.323715360094
15 479.63127526041376
10 378.9333879565738
19 1149.0329697621244
15 648.5212239205142
```

Expected output
```
711360
```

