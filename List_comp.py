#This code is to represent large data from int to float by dividing 10

temps = [234, 585, 234, 345]
new_temp = []
for temp in temps:
    new_temp.append(temp/10)

print(new_temp)

#Same thing can be written in other way as well
new_temp1 = [temp/10 for temp in temps]
print(new_temp1)

temp1 = [234, 554, 234, 564, -9999, 234]
new_temp2 = [temp/10 for temp in temp1 if temp != -9999]
print(new_temp2)