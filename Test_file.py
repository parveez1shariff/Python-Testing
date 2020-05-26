#This code to read a file

myfile = open("original.txt", mode='r')
print(myfile.read())

# Closing the file
myfile1 = open("original.txt")
content = myfile1.read()

myfile1.close()
print(content)

# The below code is to use "With" function

with open("original.txt") as myfile2:
    content1 = myfile2.read()

print(content1)

# The below code is to write in to the file
with open("Vegetable.txt", mode='w') as myfile3:
    myfile3.write("How are you?\n I am fine")




# This code is to open file and append and read
with open("Vegetable.txt",'a+') as myfile:
    myfile.write("\nHoney")
    myfile.seek(0)
    content = myfile.read()
print(content)

