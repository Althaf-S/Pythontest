from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")
input_file = open(from_file)
inputdata = input_file.read()
print(f"The input file is {len(inputdata)} bytes long")
print(f"Does the output file exist? {exists(to_file)}")
print("Hit RETURN to continue, CTRL-C to abort.")
input()
output_file = open(to_file, 'w')
output_file.write(inputdata)
print("Alright, all done.")
output_file.close()
input_file.close()
