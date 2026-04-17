''' FUNCTIONS
(1) DEFINE vs CALL
(2) Pramaetr vs Argument
(3) Keyword & default arguments
(4) Scope
'''

print("==== DEFINE (parametr) vs CALL (argument) ====")
# build in function > print() type()
# Function - reusable block of code!
# Instead of block {} in Java, Python uses indentation!


# Define - build, parametr
def greet(a):
    print(f"How do you do, {a}")

def greeting (b):
    print("greeting is executed")
    return f"Hi {b}"

# CALL - Execute
result1 = greet('Martin')
print("result1:", result1)


result2 = greeting("Justin")
print("result2:", result2)