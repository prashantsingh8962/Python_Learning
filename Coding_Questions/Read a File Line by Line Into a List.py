Example 1: Using readlines()
Let the content of the file data_file.txt be

honda 1948
mercedes 1926
ford 1903
Source Code

with open("data_file.txt") as f:
    content_list = f.readlines()

# print the list
print(content_list)

# remove new line characters
content_list = [x.strip() for x in content_list]
print(content_list)
Run Code

==>Output:
['honda 1948\n', 'mercedes 1926\n', 'ford 1903']
['honda 1948', 'mercedes 1926', 'ford 1903']



Example 2: Using for loop and list comprehension
with open('data_file.txt') as f:
    content_list = [line for line in f]

print(content_list)

# removing the characters
with open('data_file.txt') as f:
    content_list = [line.rstrip() for line in f]

print(content_list)


==>Output:
['honda 1948\n', 'mercedes 1926\n', 'ford 1903']
['honda 1948', 'mercedes 1926', 'ford 1903']
