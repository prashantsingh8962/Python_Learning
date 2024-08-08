Example 1: Using os module
import os

file_stat = os.stat('my_file.txt')
print(file_stat.st_size)

==>Output: 34



Example 2: Using pathlib module
from pathlib import Path

file = Path('my_file.txt')
print(file.stat().st_size)

==>Output: 34
