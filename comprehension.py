'''Comprehension
(1) What is comprehension & list comp
(2) set and dicyionary comp.
'''

print("======  What is comprehension & list comp ======")
# Comprehinsion acts like spread operator!

'''Comprehension general systax:
a) *iterable
b) <expression> for item in iterable
c) <expression>  for item in iterable <condition>
'''

#list comp.
numbers = [1, 2, 4, 2, 1, 20]
list_numbers = [*numbers] # a version

print("list_numbers:", list_numbers)
print(numbers is list_numbers)
print(id(numbers), id(list_numbers))

print("---------")
people = [("Robert", 21), ("Steve", 19), ("Tony", 25)]
list_people = [person[0] for person in people] # b version 
print("list_people:", list_people)

print("---------")
cars = [
    ("Ferrari", 78),
    ("Tayota", 87),
    ("Audi", 119),
    ("BMW", 109),
    ("Pagani", 33),
]
list_cars = [car[0] for car in cars if car[1] > 80] # c version
print("list_cars:", list_cars)


print("========= set and dicyionary comp ========")
numbs = [1, 5, 4, 20, 4, 5, 1, 4]
set_numbs = {*numbs}
print("set_numbs:", set_numbs)

dict_people2 = {person[0]: person[1] for person in people if person[1] > 20} # d version
print("dict_people2:", dict_people2)

# (<expression> for item in iterable genetic)