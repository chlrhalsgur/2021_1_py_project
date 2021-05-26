import requests
from bs4 import BeautifulSoup

# url = 'https://comic.naver.com/webtoon/list.nhn?titleId=748105&weekday=thu'
# #headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
# res = requests.get(url)
# res.raise_for_status()

# soup = BeautifulSoup(res.text,'lxml')
# cartoons = soup.find_all('td', attrs={'class':'title'})
# title = cartoons[0].a.get_text()
# print(title)


url = 'https://understat.com/league/EPL'
headers = {"User-Agent":"Mozilla/5.0"}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

title = soup.select('div.page-wrapper > div')
print(title)