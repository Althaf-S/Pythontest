from sys import argv

script, filename = argv
f = open(filename)
print(f"Here's is the data in your file {filename}:")
print(f.read())
print("Type your filename again:")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())
