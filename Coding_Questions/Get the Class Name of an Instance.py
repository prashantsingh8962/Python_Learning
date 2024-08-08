Example 1: Using __class__.__name__
class Vehicle:
    def name(self, name):
        return name

v = Vehicle()
print(v.__class__.__name__)

==>Ouput: Vehicle


Example 2: Using type() and __name__ attribute
class Vehicle:
    def name(self, name):
        return name

v = Vehicle()
print(type(v).__name__)

==>Ouput: Vehicle
