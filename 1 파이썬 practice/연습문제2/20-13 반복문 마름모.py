n = int(input("마름모의 크기(숫자)를 입력하세요 : "))
for i in range(1, n+1):
    print(" "* (n-i), "*" * (2*i-1))
for j in range(n-1, 0, -1) :
    print( " "* (n-j), "*" * (2*j-1))