from urllib import request

target = request.urlopen("http://hanbit.co.kr")
content = target.read()

print(content)