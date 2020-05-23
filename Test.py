import datetime
x = datetime.datetime.now()
print("The date and time is:", x)

mynumber = 10
mytext = "hello"

print(mynumber, mytext)

color_codes = ((2,3,4), (3,4))
print(color_codes)
print(type(color_codes))

#This dictionary contains tuple type 
day_temperatures = {"morning":(34.25,34.65,23.5), "noon":(23.45,65.4,34.35), "evening":(23.1,34.3,45.4)}
print(day_temperatures)

#This to test access the items of list
serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
temp = serials[0]
temp1 = serials[2]
temp2 = serials[5]
serials.clear()
serials = [temp, temp1, temp2]
print(serials)

print(Mean_Fun([3, 4, 5]))