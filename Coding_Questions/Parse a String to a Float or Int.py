Example 1: Parse string into integer
balance_str = "1500"
balance_int = int(balance_str)

# print the type
print(type(balance_int))

# print the value
print(balance_int)

==>Output: 
<class 'int'>
1500


Example 2: Parse string into float
balance_str = "1500.4"
balance_float = float(balance_str)

# print the type
print(type(balance_float))

# print the value
print(balance_float)

==>Output:
<class 'float'>
1500.4


Example 3: A string float numeral into integer
balance_str = "1500.34"
balance_int = int(float(balance_str))

# print the type
print(type(balance_int))

# print the value
print(balance_int)

==>Output: 
<class 'int'>
1500
