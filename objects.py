'''OBJECTS
    (1) What is objects
    (2) Iterable objects & RANGE
    (3) DICTIONARY
    (4) Error handling system
'''

import array # package/module
import math
from math import ceil, asin
print("==== What is objects ====")
# An objects has state and method properties
# Everything is object in Python!

print (type('Hello world!'))
print(type(100))
print(type(True))
print(type(array))
print(type(math))

# Paradigm > OOP & Functional programming
# OOP 4 CONCEPTS > Abstaction | Encapsulation | Inheritence | Polimorphism
result = math.ceil(97.7) # CALL
print("result1:", result)

result2 = ceil(98.7)
print("result2:", result2)
