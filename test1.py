# !/usr/bin/env python3
# Anchor extraction from HTML document

# pip install bs4 해줘야 함
# html.parser를 이용해서 분석한다.

from bs4 import BeautifulSoup
from urllib.request import urlopen

# response에 url을 넣는 다는 의미

response = urlopen('https://understat.com/league/EPL')
soup = BeautifulSoup(response, 'html.parser')
select = soup.select(".align-right")
print(select[0])

# f = open("새파일.txt", 'w')
# for anchor in soup.select("td.goal"):
#     data = anchor.get_text()+"\n"
#     f.write(data)
# f.close()
# for anchor in soup.select("span.iconize iconize-icon-left")    

# writedata.py

