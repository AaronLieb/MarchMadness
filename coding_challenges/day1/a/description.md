# Day 1 - Parsing People - Part A

ACM at CSUF hosted a workshop on string parsing.

There was a huge turnout, and we enforced a strict security
policy, requiring each person to go through a security check-in before entering
or leaving the event.

To help us keep track of everyone, we brought on an unpaid security intern.
This intern was very diligent and didn't miss a single person, and kept logs of
every time someone entered or exited.

Now, the CSUF Computer Science department needs to know how large of a room to
book for future events, and they've asked for the maximum number of people who
were in the room at any one time during the workshop.

That's where you come in! We're enlisting your exceptional computer programming
skills to help us parse through the logs and find the answer to this important
question.

## Input

The first line contains an integer `n`, representing total number of lines in the log.

The next `n` following lines each contain a phrase describing what the security
intern saw. Each phrase will be in the format "[name] entered/left the room".

Names are case-sensitive and contain only alphabetic characters, with no spaces.

No two people have the same name. A person can enter and exit a room as many
times as they like, but cannot exit the room if they are not inside of it.

## Output
What was the maximum number of people in the room at one time?

## Examples

Input
```
16
Hilda entered the room
Amy entered the room
Julio entered the room
Julio left the room
Norma entered the room
Crystal entered the room
Julio entered the room
Hilda left the room
Matthew entered the room
Matthew left the room
Julio left the room
Tyson entered the room
Crystal left the room
Amy left the room
Tyson left the room
Norma left the room
```

Expected Output
```
5
```

Input
```
14
Sharon entered the room
Brady entered the room
Thomas entered the room
Minnie entered the room
Katherine entered the room
Katherine left the room
Greg entered the room
John entered the room
Sharon left the room
Thomas left the room
John left the room
Brady left the room
Minnie left the room
Greg left the room
```

Expected Output

```
6
```

## Constraints
`n <= 20000`


