Example1: Program to Compute LCM
# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))

==>Output: The L.C.M. is 216

Example2: Program to Compute LCM Using GCD
#Number1 * Number2 = L.C.M. * G.C.D.
# Python program to find the L.C.M. of two input number

# This function computes GCD 
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

num1 = 54
num2 = 24 

print("The L.C.M. is", compute_lcm(num1, num2))

==>Output: The L.C.M. is 216

Example3: function to calculate the lowest common multiple (LCM) of two numbers.
import math

def lcm(a, b):
    # Calculate the GCD of a and b
    gcd = math.gcd(a, b)
    
    # Calculate the LCM using the formula
    lcm = abs(a * b) // gcd
    
    return lcm

# Example usage
a = 12
b = 15
print(f"The LCM of {a} and {b} is {lcm(a, b)}")

==>Output: The LCM of 12 and 15 is 60

