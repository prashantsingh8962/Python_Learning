Example 1: Reverse a Number using a while loop
num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))

==>Output: 4321



Example 2: Using String slicing
num = 123456
print(str(num)[::-1])

==>Output: 654321
