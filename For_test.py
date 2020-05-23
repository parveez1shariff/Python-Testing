#Testing for loop

temarature = input("Enter today's three temparture records:")
print(type(temarature))

temparature = [23.4, 45.23, 12.8]
for temp in temparature:
    print(round(temp))

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for temp in colors:
    if isinstance(temp, int):
        print(temp)


        