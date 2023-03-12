#! /usr/bin/bash
#
if [ -d "outputs" ]
then
  echo "Clearing outputs directory"
  rm -rf "./outputs"
fi

mkdir "./outputs"

echo "Running solution... [0.in, 99.in]"
for i in {0..99}
do
  python solve.py < "../inputs/$i.in" >> "results.out"
done
