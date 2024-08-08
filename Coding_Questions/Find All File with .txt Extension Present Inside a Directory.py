Example 1: Using glob
import glob, os

os.chdir("my_dir")

for file in glob.glob("*.txt"):
    print(file)

==>Output: 
c.txt
b.txt
a.txt


Example 2: Using os
import os

for file in os.listdir("my_dir"):
    if file.endswith(".txt"):
        print(file)

==>Output: 
a.txt
b.txt
c.txt



Example3:Using os.walk
import os

for root, dirs, files in os.walk("my_dir"):
    for file in files:
        if file.endswith(".txt"):
            print(file)

==>Output: 
c.txt
b.txt
a.txt
