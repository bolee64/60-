b3 = [i for i in range(1,21)]

def f1(x) : return x*x
f2 = lambda x : x*x

map(f1, b3)
print(f1)

a = list(map(f1, b3))

b = list(map(f2, b3))

c = list(map(lambda x : x*x, b3))

d = list(map(lambda x : x+x, b3))

print(a)
print(b)
print(c)
print(d)

b4 = [i for i in range(1,101)]
f3 = lambda x : x % 2 == 0
e = list(filter(f3, b4))
f = list(filter(lambda x : x % 2 == 1, b4))
g = list(filter(lambda x : x % 3 == 0, b4))

h = (lambda x, y : x+y)
print(h(10,20))