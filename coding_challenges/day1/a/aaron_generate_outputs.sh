#!/bin/bash
for i in {0..99}
do
  python solve.py < "inputs/$i.in" >> aaron.out
done
