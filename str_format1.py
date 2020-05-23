# Multple string formating

name = input("Enter your name:")
surname = input("Enter your surname:")

message1 = "Hello %s %s" % (name, surname)
message2 = f"Hello {name} {surname} whats up today!"

print(message1)
print(message2)
print(type(message1))