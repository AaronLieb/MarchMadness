#! /usr/bin/bash
for i in {0..99}
do
  python solve.py > "inputs/$i.in" 2>> "results.out"
done
echo "Donezo"
