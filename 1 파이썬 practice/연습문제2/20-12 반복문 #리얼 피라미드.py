#리얼 피라미드

line= int(input('number:'))

print('------pyramid-----')

for star in range(1, line+1):
    print(' ' * (line - star) + '*' * (2 * star -1))

print('-----end-----')