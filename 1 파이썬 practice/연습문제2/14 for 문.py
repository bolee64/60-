a = [1,2,3,4]

for num in a:
    print(num*3)
result =[num*3 for num in a]
print(result)
print(type(result))
print(type(num))
print(type(a))