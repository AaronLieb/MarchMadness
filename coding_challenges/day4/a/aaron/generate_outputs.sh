#! /usr/bin/bash
echo "Running solution... [0.in, 99.in]"
for i in {83..99}
do
  if [  $((i % 10)) -eq 0  ]
  then
    echo $i
  fi
  python solve.py < "../inputs/$i.in" >> "results.out"
done
echo "Donezo"
