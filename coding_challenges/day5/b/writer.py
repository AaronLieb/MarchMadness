from generate import generateOne

inputs_dir = 'inputs/'
output_file = 'results.out'

for i in range(100):
    if i % 1 == 0:
        print(f'{i/100*100:.2f}%')
    # open new file
    out, err = generateOne()
    with open(inputs_dir + str(i) + '.in', 'w') as wr:
        wr.write(out)

    with open(output_file, 'a') as of:
        of.write(err)
