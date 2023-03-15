# Day 3 - Leaving Lisbon Faster - Part B

Monokai had a close call with the police and has decided to use a new strategy
to help him avoid potential capture.

Monokai is again trying to leave Libson! Heres his new plan:

1) He wants to get to his destination as fast as possible.
2) He can't be in a city for more than 3 hours

Monokai has collected a list of all upcoming flights.

Hopefully this new strategy will keep the authorities clueless!

## Input
The first two lines contain Monokai's `starting` and `ending` city. Of course,
Monokai starts in Lisbon!

The next line of input is an integer `n` which represents the number of
available flights.

Each of the `n` following lines contains two space-separated cities `u` and
`v` and two `hours:minutes`/`hh:mm` times `w` and `d`.

Monokai can take a flight from `u` to `v` and the duration of the flight will be `d`.
The time he needs to wait beofre the flight takes off is `w`. (This means that the total time would be `d` + `w`)

`d` and `w` are not absolute times, but relative times (durations).

## Output

Given Monokai took the most optimal flights, what is the time (in minutes) that
the entire journey would take for him to get from Lisbon to his destination?

However, be careful! Monokai can not stay in one city for more than 3 hours.

## Constraints
`25 <= N <= 100`

## Examples

Input
```
Lisbon
Douane
25
Douane Thonex 08:43 02:15
Chokwe Douane 07:30 01:15
Thonex Omarska 00:40 02:33
Lisbon Douane 06:59 00:17
Chokwe Omarska 00:37 02:35
Douane Chokwe 07:44 04:01
Thonex Lisbon 02:56 04:30
Chokwe Douane 00:04 04:06
Lisbon Thonex 03:57 00:19
Chokwe Thonex 00:02 00:43
Chokwe Omarska 02:47 00:10
Douane Chokwe 03:16 04:37
Lisbon Thonex 06:24 04:30
Chokwe Thonex 00:36 03:32
Omarska Douane 02:10 03:57
Omarska Chokwe 02:14 01:05
Lisbon Chokwe 01:10 02:05
Omarska Thonex 09:22 03:05
Douane Lisbon 00:26 04:45
Thonex Lisbon 02:27 01:49
Chokwe Lisbon 09:18 00:54
Thonex Chokwe 00:18 00:53
Douane Omarska 03:02 00:11
Omarska Thonex 01:50 02:31
Chokwe Omarska 02:38 01:36
```

Expected output
```
445
```

Input
```
Lisbon
Vares
25
Pirdop Kosciusko 09:53 00:32
Kosciusko Modale 10:00 02:54
Pirdop Kosciusko 06:49 00:21
Lisbon Vares 08:28 04:18
Pirdop Vares 02:40 01:04
Vares Pirdop 02:24 02:48
Kosciusko Vares 02:24 04:49
Lisbon Vares 01:56 00:54
Kosciusko Vares 06:23 05:00
Pirdop Kosciusko 00:44 01:30
Lisbon Kosciusko 09:17 04:11
Modale Vares 03:34 03:49
Modale Vares 00:24 00:45
Vares Modale 06:37 02:23
Lisbon Kosciusko 06:57 02:03
Pirdop Vares 01:45 02:41
Pirdop Lisbon 09:08 00:54
Vares Kosciusko 06:14 02:50
Lisbon Modale 01:46 03:56
Modale Kosciusko 05:42 01:25
Pirdop Lisbon 01:32 04:19
Vares Modale 01:50 00:31
Modale Kosciusko 05:46 00:51
Kosciusko Modale 05:53 03:45
Pirdop Lisbon 05:11 01:05
```

Expected output
```
170
```
