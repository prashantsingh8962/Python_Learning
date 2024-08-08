Example 1: Using a for loop
The content of the file my_file.txt is

honda 1948
mercedes 1926
ford 1903

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print(file_len("my_file.txt"))

==>Output: 3



Example 2: Using list comprehension
num_of_lines = sum(1 for l in open('my_file.txt'))

print(num_of_lines)

==>Output: 3
