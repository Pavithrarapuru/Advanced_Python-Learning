# Functions functions is a reuasable block of ccode. We can call it wwhenever we want.

def greet():
    print("hello")
greet()    

def greet(name):
    print(name)
greet("Python")    

def add(a,b):
    print(a+b)
add(2,3)    

def square(num):
    return(num*num)
res = square(5)
print(res) 

def cube(num):
     return num*num*num
res = cube(3)
print(res)

def cube(num):
    return num * num * num

result = cube(2)

print(result)

def emp(name,age,role):
    print(name,age,role)
emp('pavithra','Gen AI engineer',23)  
emp('pavithra',23, 'Gen AI engineer')   # Positional arguments

def emp(name,age,role):
    print(name,age,role)

emp(
    name="Pavithra",
    age=23,
    role="Python"
)


# *args
def add(*args):
    print(args)
add(10,20,30)

# *Kwargs
def add(**kwargs):
    print(kwargs)
add(
    name='pavithra',
    age = 23,
    role="gen ai"
)  

# Positional-Only Arguments

def sum(a,b, /):
    return a+b
res = sum( 2,3,)
print(res)

# keyword-only Arguments

def sum(a,*,b,c):
    return a+b+c
res = sum(1,b=2,c= 3)
print(res)

# Function Scope

def val():
    x = 10
    print(x)
val()  
x = 20   
def val():
    print(x)
val()
x = 30
def val():
    print(x)
val()    

# return calling function

def outer():

    def inner():
        print("Hello from inner")

    return inner

# CLOSURES
#Closures are one of the more advanced function concepts.

#A closure occurs when an inner function remembers variables from the outer function, even after the outer function has finished executing.
def multiplier(x):

    def multiply(y):
        return x * y

    return multiply

double = multiplier(2)
print(double)

# Lambda
# lambda is an anonymus function
def sqa(num):
    return num*num
r = sqa(2)
print(r)

# In Lambda

sqa = lambda x: x*x
print(sqa(5))

nums1 = [1,2,3]
squares = list(map(lambda x: x*x, nums1))
print(squares)


# Map Function

nums = [1,2,3,4,5]
def sq(x):
    return x*x
res = map(sq, nums)
print(list(res))

# Filter
cart = [1,2,3,4,5,6,7,8,9,10]
def even(x):
    return x%2 == 0
res = filter(even, cart)
print(list(res))

# reduce apply a same function multiple tyms and returns a single value on a specific condition
from functools import reduce
cart1 = [1,2,3,4,4,5]


res = reduce(lambda a,b: a+b,cart1)
print(res)

# Recursion

# Recursion means a function call itself

def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)
countdown(5)    

def fact(n):
    if n == 1:
        return 1
    return n *fact(n-1)
print(fact(5))

# Function annotations
# this  function annotations allows us to write extra info about the function like same as the description
def add(a,b):
    return a+b
res = add(2,3)
print(res)  # Normal

def add(a:int,b:int) -> int:
    return a+b
res = add(2,3)
print(res)  # Annotations

# type Hints

def emp(name,age,role):
    return f"{name} is a {age} years old and working as a{role}"

rez = emp('pavithra',23, 'gen Ai developer')
print(rez)


# DECORATOR
# with the help of decorators we ca add or extend   the behaviour of a function without modification of the code

def greet():
    print("hello")
greet()               # Normal 

def decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper
greet = decorator(greet)
greet()

# GENERATORS
# generators  is a special type of function used to generate ONE value at a time instead of  all values at a time
# the keyword we use for generators is YIELD

# PARTIALLY
# creates another fucntion by fixing some arguments of an existing function  in advance 


from functools import partial

def multiply(a, b):
    return a * b

double = partial(multiply, 2)