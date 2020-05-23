a = {1,2,'a'}

print(a)

i = 'n'
if isinstance(i, int):
    i+=1
    print(i)
elif isinstance(i, str):
    i = int(i)
    i+=1
    print(i)

