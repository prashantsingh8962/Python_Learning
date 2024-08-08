Example 1: Using yield
def split(list_a, chunk_size):

  for i in range(0, len(list_a), chunk_size):
    yield list_a[i:i + chunk_size]

chunk_size = 2
my_list = [1,2,3,4,5,6,7,8,9]
print(list(split(my_list, chunk_size)))

==>Output: [[1, 2], [3, 4], [5, 6], [7, 8], [9]]


Example 2: You can do the same thing using list compression as below.
chunk_size = 2
list_chunked = [my_list[i:i + chunk_size] for i in range(0, len(my_list), chunk_size)]
print(list_chunked)

==>Output: [[1, 2], [3, 4], [5, 6], [7, 8], [9]]


Example 3: Using numpy
import numpy as np

my_list = [1,2,3,4,5,6,7,8,9]
print(np.array_split(my_list, 5))

==>Output: [array([1, 2]), array([3, 4]), array([5, 6]), array([7, 8]), array([9])]
