# applying for loop for the dictorary

student_grades = {"John": 23.5, "Jack": 78.5, "haan": 45.3}
for grades in student_grades.items():
    print(grades)

phone_numbers = {"Parveez": 7829200515, "Taj": 9008109303}
for phone in phone_numbers.items():
    print("{} has a phone number {}".format(phone[0], phone[1]))

for key, value in phone_numbers.items():
    print("{} has a phone number {}".format(key, value))

#Trying to replace number + with 00
phone_numbers1 = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for number in phone_numbers1.values():
    temp =  number[1:]
    z = "0"
    print(type(z))
    print(type(temp))
    temp1 = z+temp
    print(temp1)
