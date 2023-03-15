# Day 3 - Leaving Lisbon - Part A

Upset with the local politics, Monokai is trying to leave Lisbon! Monokai wants
to take a series of flights to evade the local authorities and arrive at a
final destination. Monokai is requesting your help in determining how `elusive`
his travel plans are.

Here's how Monokai wants you to determine `elusive`-ness:

1) If a city you are traveling to has a longer name than the city you
are traveled from, increase `elusive`-ness by
`5`.

2) If a city you are traveling to has a shorter name than the city you
are traveled from, decrease `elusive`-ness
by 2.

3) If a city you are traveling to has a name of the same length as the city you
traveled from, do not modify `elusive`-ness.

Due to the aftermath of World War 7, there exists strict border laws. You may
only take direct flights from one city to another as per the available flights
(your input).

## Input
The first two lines contain Monokai's `starting` and `ending` city. Of course,
Monokai starts in Lisbon!

The next line of input is an integer `n` which represents the number of
available flights.

Each of the `n` following lines contains two space-separated cities `u` and
`v`. You may travel from `u` to `v` but not from `v` to `u` directly.

## Output
How `elusive` Monokai's travel plans are.

## Constraints
`1000 <= N <= 10000`

`elusive`-ness starts at 0 and `abs(elusive)` < 2^31.

## Examples

Input
```
Lisbon
Fircrest
16
Fircrest Rufus
Lejanias Ubud
Mekele Tagum
Rufus Villagrande
Karori Lejanias
Balabanovo Letschin
Lisbon Villamalea
Tagum Toporu
Goodno Karori
Letschin Goodno
Karabaglar Fircrest
Villamalea Karabaglar
Toporu Balabanovo
Sangamner Barkhera
Villagrande Sangamner
Barkhera Mekele
```

Expected output
```
1
```

Input
```
Lisbon
Kunda
92
Millbrook Poboru
Ghyvelde Chocianow
Metten Kirchseeon
Hext Papao
Madeira Apensen
Ottershaw Tiszafoldvar
Jhanjharpur Maze
Ivanava Whipholt
Reisbach Alterhofen
Freienbach Rossett
Dolneni Beuvrages
Fujikawaguchiko Qabil
Azatan Ileana
Jinja Madeira
Kailashahar Glashutten
Dunken Premariacco
Dernekpazari Kailashahar
Trilj Ghyvelde
Bernissart Kuvandyk
Tormac Pithora
Irbin Tormac
Zahl Nanning
Tiszafoldvar Nazarovo
Goldsmith Trilj
Makkum Benfeld
Bezdead Rayevskaya
Dondaicha Dorpen
Udaipura Kawit
Harrietta Ivanava
Piscu Weinbohla
Glashutten Dondaicha
Tokeland Poroshkovo
Weinbohla Batetskiy
Batetskiy Save
Summerland Sevan
Nazarovo Jhanjharpur
Gavirate Slatino
Tarakan Halaucesti
Weilerbach Hext
Papao Tarakan
Chocianow Toshbuloq
Kendrick Tokeland
Dorpen Pelabuhanratu
Tilaran Valko
Qiaogu Sanza
Alterhofen Azatan
Salpazari Millbrook
Sandersville Freienbach
Rayevskaya Fujikawaguchiko
Pithora Bernissart
Lauterbach Bezdead
Poysdorf Bordighera
Nanning Kendrick
Poboru Qiaogu
Justus Ottershaw
Qabil Summerland
Valko Zahl
Machynlleth Katherine
Katherine Gavirate
Baric Sandersville
Urkut Sheksna
Bordighera Hanzhong
Poroshkovo Casarrubuelos
Premariacco Urkut
Spade Goldsmith
Slatino Kerrick
Maze Jinja
Halaucesti Kunda
Sheksna Piscu
Save Lauterbach
Kerrick Dolneni
Casarrubuelos Dunken
Sevan Salpazari
Hanzhong Weilerbach
Lisbon Machynlleth
Kawit Makkum
Apensen Irbin
Rossett Poysdorf
Sanza Butgenbach
Toshbuloq Udaipura
Butgenbach Westby
Westby Canmore
Kirchseeon Osie
Pelabuhanratu Harrietta
Whipholt Spade
Beuvrages Baric
Kunda Dernekpazari
Kuvandyk Tilaran
Osie Till
Canmore Metten
Benfeld Justus
Till Reisbach
```

Expected output
```
-29
```
