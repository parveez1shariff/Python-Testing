#Testing While loop

user_name = ''
password = ''
while user_name != "Jack":
    user_name = input("Enter the user name:")

count = 3

while password != "78#stw" and count > 0:
    password = input("Enter password:")
    count = count - 1
    print(count)
    print("password incorrect")
