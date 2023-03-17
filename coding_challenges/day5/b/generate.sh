if [ -d "inputs" ]
then
  echo "Clearing ./inputs..."
  rm -rf inputs
  echo "Creating empty ./inputs..."
  mkdir inputs
fi

if [ -f "results.out" ]
then
  echo "Clearing results.out"
  rm results.out
  touch results.out
fi

echo "Generating..."
python writer.py
echo "Done"
