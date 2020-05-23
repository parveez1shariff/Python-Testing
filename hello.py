print('Hello, World')
a = 4
print(a)
b = 5
print(b)
pi = 3.14
print(pi)
c = 'A'
print(c)
name = 'Jack'
print(name)

q = True
print(q)

x = None
print(x)

print(type(a))
print(type(b))
print(type(pi))
print(type(c))
print(type(name))
print(type(q))
print(type(x))

a, b, c = 1, 2, 3
print(a,b,c)

a, b, _ = 1,2,3
print(a,b)

x = y = [7, 8, 9]
x = [13,34,45]
print(y)
print(x)

x = y = [2,3,4,5]
x[0] = 23
print(y)
print(x)

x = [1,2,[3,4,5,6],2,4,5]
print(x)
print(x[0])
print(x[2][1])
