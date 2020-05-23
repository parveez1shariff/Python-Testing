#Formatting the string

user_input = input("Enter your Name: ")
message1 = "Hello %s"  %user_input
message2 = f"Hello {user_input}"

print(message1)
print(message2)