l = []
for i in range(2,10):
    for j in range(1,10):
        if(i != 4):
            l.append(i*j)
print(l)

print([ i*j for i in range(2,10) for j in range(1,10) if(i != 4)])
print(type(in))