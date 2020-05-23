# This code is to build the lisener

def Sentance_maker(phrase):
    capitalized = phrase.capitalize()
    interrogation = ("how","what","when","why")
    if phrase.startswith(interrogation):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []
while True:
    user_input = input("Say something: ")
    if user_input == '\end':
        break
    else:
        results.append(Sentance_maker(user_input))

print(" ".join(results))


