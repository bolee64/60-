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


