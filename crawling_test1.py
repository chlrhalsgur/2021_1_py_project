from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import Beautifulsoup


search = input('')
url = 'https://1xbet.whoscored.com/Statistics'
html = urlopen(url).read()
soup = Beautifulsoup(html,'html.parser')

play_time = 'minsPlayed   '

print(play_time[0])


print("ss")