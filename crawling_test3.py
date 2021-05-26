import requests
from bs4 import BeautifulSoup


url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20210525&tg=1'
headers = {"User-Agent":"Mozilla/5.0"}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')
title = soup.select('td.title > div.tit5 > a')
point = soup.select('td.point') 

# for t in title:
#     print(t.getText())
# for p in point:
#     print(p.getText())

for t, p in zip(title, point):
    print(t, '+', p)

