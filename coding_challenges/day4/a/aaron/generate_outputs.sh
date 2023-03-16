#! /usr/bin/bash
echo "Running solution... [0.in, 99.in]"
for i in {0..99}
do
  python solve.py < "../inputs/$i.in" >> "results.out"
done
echo "Donezo"
