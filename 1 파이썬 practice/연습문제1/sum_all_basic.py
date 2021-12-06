# 함수를 선언합니다.
def mul(start, end, step):
    # 변수를 선언합니다.
    output = 1
    # 반복문을 돌려 숫자를 더합니다.
    for i in range(start, end, step):
        output *= i
    # 리턴합니다.
    return output

# 함수를 호출합니다.
print(mul(5, 17, 2))


