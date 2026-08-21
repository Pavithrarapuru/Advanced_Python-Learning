# File handling
# File  is a Named location where we stored information in the storage device permanently (Persistance Storage)
# File handling means perform operation son files such as cretaing, reading, writing, updating, closing .

# There are two types of files (TEXT and BINARY)
# Text files(human readable text) .txt,.csv.html
# Binary Files (Store data in the form of raw bytes) .jpg,.png,.mp4
# Binary files can be read using the command rb.
with open("photo.png", "rb") as file:
    data = file.read()

# Reading the File
file = open("data.txt", "r")
lines = file.read()             # returns the entire file in string format
lines = file.read(n)      # returns the string in with limited characters
lines = file.readline()   # return the string only one line at a time
lines = file.readlines()   # returns all the lines in the form of LIST
for line in file:     # it will iterates each line and process it and go for next line
    print(line) 

# Writing a file

file = open("data.txt", "w")
file.write("Python")
file.write(100) # won't work
file.write(str(100))
file.close()
file.writelines([
    "python\n",
    "java\n"
])    


# CLosing the file 
file.close()
print(file.close)   # trus if the file is closed  pr False if the file is opened

# Flush when we writw something to the file, it is not directly send the code to file it will stor ein a temporary location and after that the flush tell the python send this data in buffer ot the file
file = open("data.txt", "w")

file.write("Hello Python")

file.flush()

file.close()