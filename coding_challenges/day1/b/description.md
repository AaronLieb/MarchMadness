# Day 1 - Parsing People - Part B

This is a continuation of Part A

After the success of the previous event, ACM decided to host another string
parsing workshop. People must really love strings!

They decided to keep their strict security policy of logging all of people
coming in and out of the event.

ACM expected an even higher turnout than last time.
One unpaid security intern wasn't enough, so this time they had three!

* Firewall Frankie
* Cryptography Claire
* Hacker Hank

Firewall Frankie is a perfectionist and has perfect memory. Any logs from
Frankie contain all of the names of the people passing by.

Crypography Claire is new and doesn't know anyone's names. She just writes down
the number of people she saw walk through.

Hacker Hank is lazy and doesn't want to write down all the names. He writes
the name of the first person he saw in each group, and then writes the
number of people that followed.

All three of the unpaid security interns keep their logs in the same file.

You've once again been asked to find the maximum number of people that were in
the room at one time.

## Input

The first line contains an integer `n`, representing total number of lines in the log.

The next `n` following lines each contain a phrase describing what the security
interns saw. Each phrase will be in one of three formats.

Names are case-sensitive and contain only alphabetic characters, with no spaces.

## Output
What was the maximum number of people in the room at one time?

## Examples

Input
```
8
4 people walked in
Gilbert and Donald exited the room
Holly and 2 others arrived
Karen and 3 others departed
3 people walked in
James departed
Gabriel entered the room
Clifton, Judy, Francisco and Gabriel exited the room
```

Expected Output
```
4
```

Input
```
14
Timothy and 5 others arrived
Art and 1 other departed
2 people walked in
Timothy and 1 other departed
2 people walked in
Basil, Patsy, John and Anthony exited the room
Timothy arrived
Art exited the room
William arrived
Herbert departed
Basil arrived
Basil and 2 others departed
Arturo entered the room
Arturo departed
```

Expected Output

```
6
```

## Constraints
`n <= 20000`


