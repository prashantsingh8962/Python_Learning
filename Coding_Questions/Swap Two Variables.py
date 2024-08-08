Example: Using a temporary variable
# Python program to swap two variables

x = 5
y = 10

# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

==>Output: The value of x after swapping: 10
The value of y after swapping: 5

Example: Without Using Temporary Variable
x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)

==>Output: x = 10
y = 5
