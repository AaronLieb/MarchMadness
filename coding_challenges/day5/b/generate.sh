if [ -d "inputs" ]
then
  echo "Clearing ./inputs..."
  rm -rf inputs
fi
echo "Creating empty ./inputs..."
mkdir inputs

if [ -f "results.out" ]
then
  echo "Clearing results.out"
  rm results.out
fi
touch results.out

echo "Generating..."
python3 writer.py
echo "Done"
