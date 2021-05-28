from re import findall
import requests
from bs4 import BeautifulSoup
from soupsieve import select_one
import db_test1

def crawling_movie():
    for genre_code in range(1,20):
        if genre_code == 9 or genre_code == 3:
            continue
        url = f'https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20210525&tg={genre_code}'
        headers = {"User-Agent":"Mozilla/5.0"}

        res = requests.get(url, headers=headers)
        res.raise_for_status()

        soup = BeautifulSoup(res.text,'lxml')
        title = soup.select('td.title > div.tit5 > a')
        point = soup.select('td.point') 

        for t, p in zip(title, point):
            
            db_test1.input_db('movie_list', 'movie_table', t.getText(), float(p.getText()), genre_code)
    
# crawling_movie()
