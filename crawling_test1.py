from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup


search = input('')
url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={quote_plus(search)}'

html = urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

total = soup.select('.api_txt_lines.total_tit')

print(total[0].text)


# print("ss")