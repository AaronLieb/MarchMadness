#!/bin/bash
for i in {0..99}
do
  if [  $((i % 10)) -eq 0  ]
  then
    echo "$i"
  fi
  python generate.py > "inputs/$i.in"
done
