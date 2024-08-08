Example 1: Using enumerate
my_list = [21, 44, 35, 11]

for index, val in enumerate(my_list):
    print(index, val)

==>Output: 
0 21
1 44
2 35
3 11

Example 2: Start the indexing with non zero value
my_list = [21, 44, 35, 11]

for index, val in enumerate(my_list, start=1):
    print(index, val)

==>Output: 
1 21
2 44
3 35
4 11

Example 3: Without using enumerate()
my_list = [21, 44, 35, 11]

for index in range(len(my_list)):
    value = my_list[index]
    print(index, value)

==>Output: 
0 21
1 44
2 35
3 11
