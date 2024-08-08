Example1: Solve the quadratic equation ax**2 + bx + c = 0

#**(-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

# import complex math module
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))

==>Output: Enter a: 1
Enter b: 5
Enter c: 6
The solutions are (-3+0j) and (-2+0j)


Example2: Solve the quadratic equation ax**2 + bx + c = 0
import cmath

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    d = (b**2) - (4*a*c)
    
    # Check the discriminant
    if d > 0:
        # Two distinct real roots
        sol1 = (-b + cmath.sqrt(d).real) / (2 * a)
        sol2 = (-b - cmath.sqrt(d).real) / (2 * a)
        return [sol1, sol2]
    elif d == 0:
        # One real root (repeated)
        sol = -b / (2 * a)
        return [sol,sol]
    else:
        # Two complex conjugate roots
        sol1 = (-b + cmath.sqrt(d)) / (2 * a)
        sol2 = (-b - cmath.sqrt(d)) / (2 * a)
        return [sol1, sol2]

# Example usage
a, b, c = 1, -5, 6  # Example coefficients
solutions = solve_quadratic(a, b, c)
print("Solutions:", solutions)
