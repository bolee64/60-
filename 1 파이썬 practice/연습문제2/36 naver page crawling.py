import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

plusUrl = urllib.parse.quote_plus(input('검색어를 입력하세요:'))

pageNum = 1
count = 1
 
i = input('몇페이지 크롤링 할까요?: ')

lastPage = int(i) * 10 - 9
while pageNum < lastPage + 1:
    url = f'https://https://search.naver.com/search.naver?display=15&f=&filetype=0&page=2&query={plusUrl}&research_url=&sm=tab_pge&start={pageNum}

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='sh_blog_title')

print('-----{count}페이지 결과입니다.-----')
for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
print()

pageNum += 10
count += 1