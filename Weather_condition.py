# Reading the input
def weather_contition(temp):
    if temp > 7:
        return "warm"
    else:
        return "cold"

user_input = input("Enter the temparature:")
user_input = float(user_input)
y = weather_contition(user_input)
print(y)