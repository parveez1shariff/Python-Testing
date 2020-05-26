# This code is to create a function with infinite parameter/arguments

def mean(*arg):
    Mn = sum(arg)/len(arg)
    return Mn

print(mean(2,4,9,8))

def str_infi(*arg):
    st = []
    for temp in arg:
        st.append(str(temp).capitalize())
    st.sort()

    return st 
    

print(str_infi("hello", "apple"))