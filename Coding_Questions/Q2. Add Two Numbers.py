Example 1: Add Two Numbers
# This program adds two numbers
num1 = 1.5
num2 = 6.3

# Add two numbers
sum = num1 + num2

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

==>Output: The sum of 1.5 and 6.3 is 7.8

Example 2: Add Two Numbers With User Input
# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Add two numbers
sum = float(num1) + float(num2)

# Display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

==>Output: Enter first number: 1.5
Enter second number: 6.3
The sum of 1.5 and 6.3 is 7.8


#Question.1 Write a function to calculate discount recieved.
def calculateDiscount(original_price, discounted_price):
    Discount_received = original_price - discounted_price
    return Discount_received

#Question.2 Write a function to add 10 in given no.
def add_ten(n):
    n=n+10
    return n
    
