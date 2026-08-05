# OPERATORS

# Arithemetic Operators

num1 = 5
num2 = 5
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)  # this division always returns the float value p even if the value is whole number
print(num1//num2)  # this floor division rewturns the whole value even if the value is in decimals
print(num1%num2)   # the modulus always returns the reminder value after the division
print(num1**num2)  # reutnss the power of the 2 values

# Comparison Operators  (Always returns output as True or False)

num3 = 10
num4 = 15
print("Equal:", num3==num4)
print("Not Equal:",num3 != num4)
print("greater Than:",num3>num4)
print("Less Than:",num3<num4)
print("GreaterThan or Equal:",num3>=num4)
print("LessThan or Equal:",num3<=num4)

# Assignment Operators Used to assign values or update the existing Values

Var1 = 22  # "="
print("Assign:", Var1)
Var1 += 1
print("Add n Assign:", Var1)
Var1 -= 2
print("Subtract n assign:", Var1)
Var1 *= 1
print("Multiply n assign:", Var1)
Var1 /= 2
print("Divide n assign:", Var1)
Var1 //= 2
print("Floor division n assign:", Var1)
Var1 %= 2
print("Modulus n assign:", Var1)

# Logical Operators.  Used to combine 2 or more conditions n always return true or False in the output

# AND => True if both are TRUE otherwise FALSE
a = 10
b = 5
print(a > b and a <b)

# OR => Or returns TRUE if atleast one Condition is True
print(a>b or a<0)
print(a<b or a<0)

# NOT => It returns the boolean value  EX:-  if the answer is tur it will returns False n ViceVersa

print(not(a>b))

# Membership Operators Checks weather the values exist in a collection
Area = "Banglore"
print("a" in Area)
print("c" in Area)

# Identity Operators Check weather 2 values refer to the same object or not 
a = [1,2]
b=a
print(a is b)

# Conditional Statements => it will help us to take decisions based on a condition 

Array = (1,2,3)                                    # if else
if sum(Array) == 6:
    print("Sum is Correct" )
else:
        print("Sum is InCorrect" )

age = 25                                          # nested if
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to Vote")       
  
if age > 18: print("Adult")                  # short-hand if
status = "Adult" if age >= 18 else "Minor"   # Ternary Operator 

print(status)

# LOOPS   help us to execute the sam ebloc of code repeatedly until a specific condition met 

# for loop  iterates over a sequence
Name = "python"
for i in Name:
     print(i)

for i in range(5):  # range (stop)
     print(i)  

for i in range(5,10):
     print(i)    # range(start, stop) 
for i in range(1,10,2):    # range(start,stop, step)
     print(i)   

for i in range(5):
     print("python")            
for number in range(5):
     print(number**number)


# WHILE LOOP   => it will executes as long as the condition met True condition

count = 2
while count<=2:
     print(count)
     count+=1

# Infinite Loop

#while True:
     #print("Hello")
     #break

# Break 

for i in range(10):
     if i==5:
          break
     print(i)

# CONTINUE

for i in range(15):
     if i == 5:
          continue
     print(i)     

# PASS                     just like a placeholder

for i in range(5):
     pass 


# NESTED LOOPS
for i in range(5):
     for j in range(6):
          print(i,j)

# Loop Else

for i in range(5):
     print(i)
else:
     print("loop finished")               
     



