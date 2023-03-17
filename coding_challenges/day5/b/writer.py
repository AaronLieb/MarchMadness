from generate import generateOne

inputs_dir = 'inputs/'
output_file = 'results.out'

for i in range(100):
    if i % 10 == 0:
        print(f'{i}%')
    # open new file
    out, err = generateOne()
    with open(inputs_dir + str(i) + '.in', 'w') as wr:
        wr.write(out)

    with open(output_file, 'a') as of:
        of.write(err)
