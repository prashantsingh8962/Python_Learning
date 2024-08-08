string = input()

try:
    num = int(input())
    print(string+num)
except (TypeError, ValueError) as e:
    print(e)

==>Input:                 ==>Output:
a                                 can only concatenate str (not "int") to str
2

==>Input:                 ==>Output:
a                                 invalid literal for int() with base 10: 'b'
b

#Note: The error which comes first is caught as an exception in case of multiple exceptions.
