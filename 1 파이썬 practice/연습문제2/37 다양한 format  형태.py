name = '김플'
number = 8
food = '햄버거'

print('제 이름은 '+ name + '입니다. 좋아하는 숫자는 ' + str(number) +' 이고 좋아하는 음식은 ' + food + ' 입니다.')

print('제 이름은 %s입니다. 좋아하는 숫자는 %s 이고 좋아하는 음식은 %s 입니다.' %(name, number, food))

print('제 이름은 {0}입니다. 좋아하는 숫자는 {1} 이고 좋아하는 음식은 {2} 입니다.'.format(name, number, food))

print(f'제 이름은 {name}입니다. 좋아하는 숫자는 {number} 이고 좋아하는 음식은 {food} 입니다.')