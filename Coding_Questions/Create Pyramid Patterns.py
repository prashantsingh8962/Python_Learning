Example 1: Program to print half pyramid using *
*
* *
* * *
* * * *
* * * * *

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print()


Example 2: Program to print half pyramid a using numbers
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print()

Example 3: Program to print half pyramid using alphabets
A
B B
C C C
D D D D
E E E E E

rows = int(input("Enter number of rows: "))

ascii_value = 65

for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
    
    ascii_value += 1
    print()

#Programs to print inverted half pyramid using * and numbers
Example 4: Inverted half pyramid using *
* * * * *
* * * *
* * *
* *
*

  rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    
    print()


Example 5: Inverted half pyramid using numbers
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    
    print()

#Programs to print full pyramids
Example 6: Program to print full pyramid using *
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()

Example 7: Full Pyramid of Numbers
        1 
      2 3 2 
    3 4 5 4 3 
  4 5 6 7 6 5 4 
5 6 7 8 9 8 7 6 5

rows = int(input("Enter number of rows: "))

k = 0
count=0
count1=0

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print("  ", end="")
        count+=1
    
    while k!=((2*i)-1):
        if count<=rows-1:
            print(i+k, end=" ")
            count+=1
        else:
            count1+=1
            print(i+k-(2*count1), end=" ")
        k += 1
    
    count1 = count = k = 0
    print()

Example 8: Inverted full pyramid of *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

rows = int(input("Enter number of rows: "))

for i in range(rows, 1, -1):
    for space in range(0, rows-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()

Example 9: Pascal's Triangle
           1
         1   1
       1   2   1
     1   3   3    1
   1  4    6   4   1
 1  5   10   10  5   1

rows = int(input("Enter number of rows: "))
coef = 1

for i in range(1, rows+1):
    for space in range(1, rows-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            coef = 1
        else:
            coef = coef * (i - j)//j
        print(coef, end = " ")
    print()

Example 10: Floyd's Triangle
1
2 3
4 5 6
7 8 9 10

rows = int(input("Enter number of rows: "))
number = 1

for i in range(1, rows+1):
    for j in range(1, i+1):
        print(number, end=" ")
        number += 1
    print()


