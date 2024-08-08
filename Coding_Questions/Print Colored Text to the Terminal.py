Example 1: Using ANSI escape sequences
print('\x1b[38;2;5;86;243m' + 'Prashant' + '\x1b[0m')

==>Output: Prashant


Example 2: Using python module termcolor
from termcolor import colored
#Using the module termcolor,

print(colored('Prashant', 'blue'))

==>Output: Prashant
