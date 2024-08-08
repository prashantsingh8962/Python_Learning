Open file in append mode and write to it

The content of the file my_file.txt is
honda 1948
mercedes 1926
ford 1903

with open("my_file.txt", "a") as f:
   f.write("new text")

==>Output:
honda 1948
mercedes 1926
ford 1903new text
