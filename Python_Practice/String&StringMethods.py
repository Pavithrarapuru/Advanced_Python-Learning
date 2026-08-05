string = "geeks for geeks"
print(string)
string1 = 'geeks for geeks'
print(string1)
string2 = """ Geeks for geeks 
a good platform for
coding practice"""

# Accessing the characters

fruit = "Apple"
print(fruit[3])
print(fruit[-3])

from array import array
numbers = array('i',[10,20,30])
print(numbers)


# String SLicing 
word = "Programming"
print(word[2:5])
print(word[:])
print(len(word))
print(word[::2])
print(word[::-1])
print(word[2:9:2])

# STRING METHODS


spell = " python programming "
print("uppercase:", spell.upper())
print("Lowercase:", spell.lower())
print("Capitalize:", spell.capitalize())
print("title:",spell.title())
print("swapcase:",spell.swapcase())
print("strip:",spell.strip())
print("lsstrip:",spell.lstrip())
print("rstrip:", spell.rstrip())
print("replace:", spell.replace("Python", "R"))
print("find:", spell.find("p"))
print("index:", spell.index("g"))
print("count:", spell.count("o"))
print("startswith:", spell.startswith(" " ))
print("endswith:", spell.endswith("ng"))
print("split:",spell.split())
words = ["I","Love","Python"]
print(" ".join(words))


