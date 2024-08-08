Example 1: Access both key and value using items()
dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key, value in dt.items():
    print(key, value)

==> OUtput:
a juice
b grill
c corn


Example 2: Access both key and value without using items()
dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key in dt:
    print(key, dt[key])

==>Output: 
a juice
b grill
c corn


Example 3: Access both key and value using iteritems()
dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key, value in dt.iteritems():
    print(key, value)

==>Output: 
a juice
b grill
c corn


Example 4: Return keys or values explicitly
dt = {'a': 'juice', 'b': 'grill', 'c': 'corn'}

for key in dt.keys():
    print(key)

for value in dt.values():
    print(value)

==>Output:
a
b
c
juice
grill
corn
