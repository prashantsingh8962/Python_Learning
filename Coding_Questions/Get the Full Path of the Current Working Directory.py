Example 1: Using pathlib module
import pathlib

# path of the given file
print(pathlib.Path("my_file.txt").parent.absolute())

# current working directory
print(pathlib.Path().absolute())

==>Output:
/Users/username
/Users/username



Example 2: Using os module
import os

# path of the given file
print(os.path.dirname(os.path.abspath("my_file.txt")))

# current working directory
print(os.path.abspath(os.getcwd()))

==>Output:
/Users/username
/Users/username

