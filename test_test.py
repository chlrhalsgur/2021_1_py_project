from selenium import webdriver
from pandas.io.html import read_html
import time
import pandas as pd
import numpy as np

def defensive (url, sleep_time) :
    #open webdriver
    chrome_driver = 'C:\Rselenium\chromedriver'
    driver = webdriver.Chrome(chrome_driver)
    driver.get(url)
    
    #click 'accept' button
    time.sleep(sleep_time)
    accept = driver.find_element_by_css_selector('#qcCmpButtons > button:nth-child(2)')
    accept.click()
    
    #click 'defensive' button
    time.sleep(sleep_time)
    defense = driver.find_element_by_link_text('Defensive')
    defense.click()
    
    #click 'all players' button
    time.sleep(sleep_time)
    all_player = driver.find_element_by_link_text('All players')
    all_player.click()
    
    #get the total page number
    time.sleep(sleep_time)
    page = driver.find_element_by_link_text('last')
    total_page = int(page.get_attribute('data-page'))
    
    #create the dataframe
    df_defensive = pd.DataFrame(columns = ['Player', 'Player.1', 'Apps', 'Mins', 'Tackles', 'Inter', 'Fouls',
       'Offsides', 'Clear', 'Drb', 'Blocks', 'OwnG', 'Rating'])
    
    #crawling the table
    for i in np.arange(total_page) :
        time.sleep(sleep_time)
        table = driver.find_element_by_xpath('//*[@id="statistics-table-defensive"]')
        table_html= table.get_attribute('innerHTML')
        df2 = read_html(table_html)[0]
        df_defensive = pd.concat([df_defensive, df2], axis=0)
        driver.find_element_by_link_text('next').click()
        
    return(df_defensive)

url = 'https://1xbet.whoscored.com/Regions/252/Tournaments/2/Seasons/7811/Stages/17590/PlayerStatistics/England-Premier-League-2019-2020'
df = defensive(url, 5)
# 데이터 전처리

# data preprocessing
df = df.reset_index()
df.drop(['index','Player'] , axis=1, inplace=True)
spl = df['Player.1'].str.split(',')
name = []
for i in range(len(spl)):
    a = spl[i][0]
    name.append(a)
df['name']= name
age = []
for i in range(len(spl)):
    a = int(spl[i][1])
    age.append(a)
df['age'] = age
position1 = []
for i in range(len(spl)):
    a = spl[i][2]
    position1.append(a)
df['position1']=position1
position2 = []
for i in range(len(spl)):
    if len(spl[i]) > 3 :
        a = spl[i][3]
    else : a = np.nan
    position2.append(a)
df['position2'] = position2
df.drop('Player.1', axis =1, inplace=True)
df = df.iloc[:,[11,12,13,14,0,1,2,3,4,5,6,7,8,9,10]]
df.to_csv("C:/Rselenium/defensive.csv", sep=',')