#!/bin/bash
for i in {0..99}
do
  python generate.py > "inputs/$i.in"
done
