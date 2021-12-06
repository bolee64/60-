numbers = [273, 103, 5, 32, 65, 9, 72, 800,99]

for number in numbers:
    if number % 2 == 0:
        print("{}는 짝수입니다.".format(number))
    else:
        print("{}는 홀수입니다.".format(number))
        