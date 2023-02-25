
"""
ANS = 1
fopen() function.
Read Only ('r') : Open text file for reading
Read and Write ('r+'): Open the file for reading and writing. 
Write Only ('w') : Open the file for writing. 
Write and Read ('w+') : Open the file for reading and writing. 
Append Only ('a'): Open the file for writing.


ANS = 2
Because files are limited resources managed by the operating system, 
making sure files are closed after use will protect against hard-to-debug 
issues like running out of file handles or experiencing corrupted data. 
The best defense is always to open files with a context manager.

"""
# ANS = 3

with open("pwskills.txt", "w") as f:
    f.write("I want become a data scientist")
    f.close()
    
with open("pwskills.txt", "r") as f:
    file_read = f.read()
    print(file_read)

# ANS = 4
#the read() method returns the specified number of bytes from the file. Default is -1 which means the whole file.
f = open("demofile.txt", "r")
print(f.read())

#The readline() method returns one line from the file.
#You can also specified how many bytes from the line to return, by using the size parameter.
f = open("demofile.txt", "r")
print(f.readline())

#The readlines() method returns a list containing each line in the file as a list item.
f = open("demofile.txt", "r")
print(f.readlines())

# ANS = 5
#The with statement works with the open() function to open a file. 
# Unlike open() where you have to close the file with the close() method, 
# with statement closes the file for you without you telling it to. 
# This is because the with statement calls 2 built-in methods behind the scene – __enter()__ and __exit()__

# ANS = 6
""""
Write 
The write() method writes a specified text to the file.
Where the specified text will be inserted depends on the file mode and stream position.
"a":  The text will be inserted at the current file stream position, default at the end of the file.
"w": The file will be emptied before the text will be inserted at the current file stream position, default 0.
:- Use in bytes 
writelines 
he writelines() method writes the items of a list to the file.
Where the texts will be inserted depends on the file mode and stream position.
"a":  The texts will be inserted at the current file stream position, default at the end of the file.
"w": The file will be emptied before the texts will be inserted at the current file stream position, default 0.
:- use for list 

"""
f = open("demofile2.txt", "a")
f.write("\nSee you soon!")
f.close()


f = open("demofile2.txt", "a")
f.writelines(["\nSee you soon!"])
f.close()

