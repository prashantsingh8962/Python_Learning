Example 1: Return values using comma
def name():
    return "John","Armin"

# print the tuple with the returned values
print(name())

# get the individual items
name_1, name_2 = name()
print(name_1, name_2)

==>Output: 
('John', 'Armin')
John Armin


Example 2: Using a dictionary
def name():
    n1 = "John"
    n2 = "Armin"

    return {1:n1, 2:n2}

names = name()
print(names)

==>Output: 
{1: 'John', 2: 'Armin'}
