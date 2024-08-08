Example 1: Using del keyword
my_dict = {31: 'a', 21: 'b', 14: 'c'}

del my_dict[31]

print(my_dict)

==>Output:
{21: 'b', 14: 'c'}



Example 2: Using pop()
my_dict = {31: 'a', 21: 'b', 14: 'c'}

print(my_dict.pop(31))

print(my_dict)

==>Output:
a
{21: 'b', 14: 'c'}
