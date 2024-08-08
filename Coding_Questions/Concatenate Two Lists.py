Example 1: Using + operator
list_1 = [1, 'a']
list_2 = [3, 4, 5]

list_joined = list_1 + list_2
print(list_joined)

==>Output:
[1, 'a', 3, 4, 5]


Example 2: Using iterable unpacking operator *
list_1 = [1, 'a']
list_2 = range(2, 4)

list_joined = [*list_1, *list_2]
print(list_joined)

==>Output:
[1, 'a', 2, 3]


Example 3: With unique values
list_1 = [1, 'a']
list_2 = [1, 2, 3]

list_joined = list(set(list_1 + list_2))
print(list_joined)

==>Output:
[1, 2, 3, 'a']


Example 4: Using extend()
list_1 = [1, 'a']
list_2 = [1, 2, 3]

list_2.extend(list_1)
print(list_2)

==>Output:
[1, 2, 3, 1, 'a']
