Example 1: Using time module
import time

start = time.time()

print(23*2.3)

end = time.time()
print(end - start)

==>Output:
52.9
3.600120544433594e-05


Example 2: Using timeit module
from timeit import default_timer as timer

start = timer()

print(23*2.3)

end = timer()
print(end - start)

==>Output:
52.9
6.355400000000039e-05
