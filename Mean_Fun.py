#This function is to find the mean for type list and dictionay
def mean(x):
    if type(x) == dict:
        temp = sum(x.values())/len(x)
    else:
        temp = sum(x)/len(x)

    return temp

student_grade = {"john": 23, "hon": 56, "jack": 78}
student_grade1 = [ 24 , 34, 45]
myval = mean(student_grade1) +10
print(myval)