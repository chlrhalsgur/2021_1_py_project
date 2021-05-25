import pymysql

# sql 접속
conn = pymysql.connect(host='localhost', user = 'root', password = '0000', db='football_players', charset = 'utf8')

# 입력
# 커서잡고 -> 쿼리문 작성 -> excute -> commit
curs_input = conn.cursor()
sql_input = 'insert into players_stats(name, team)\
    values(%s, %s)'
curs_input.execute(sql_input, ('Messi', 'fcb' ))
curs_input.execute(sql_input, ('Kane', 'tot'))
curs_input.execute(sql_input, ('Hazard', 'rmd'))
conn.commit()

# 출력
# 커서 잡고(딕셔너리) -> 쿼리문 -> excute -> fetch -> 출력
curs_output = conn.cursor(pymysql.cursors.DictCursor)
sql_output = 'select * from players_stats order by age' 
curs_output.execute(sql_output)
pl_st = curs_output.fetchall()

for row in pl_st:
    print(row['name'], row['age'], row['team'])


# sql 종료
conn.close()