import pymysql

# sql 접속
# conn = pymysql.connect(host='localhost', user = 'root', password = '0000', db='football_players', charset = 'utf8')

'''
입력
접속 -> 커서잡고 -> 쿼리문 작성 -> excute -> commit -> 종료
'''
def input_db(database, table, title, point, genre_code):
    conn = pymysql.connect(host='49.169.175.135', user = 'root', password = '0000', db=database, charset = 'utf8')
    curs_input = conn.cursor()
    sql_input = f'insert ignore into {table}(title, point, genre_code) values(%s, %s, %s)'
    curs_input.execute(sql_input, (title, point, genre_code))
    conn.commit()
    conn.close()

'''
출력
커서 잡고(딕셔너리) -> 쿼리문 -> excute -> fetch -> 출력
'''
def print_db():
    movie_list = []
    conn = pymysql.connect(host='49.169.175.135', user = 'root', password = '0000', db='movie_list', charset = 'utf8')
    curs_output = conn.cursor(pymysql.cursors.DictCursor)
    sql_output = 'select * from movie_table' 
    curs_output.execute(sql_output)
    movie = curs_output.fetchall()

    for row in movie:
        movie_list.append([row['title'], row['point'], row['genre_code']])
    conn.close()
    return movie_list
    
# print(print_db())


# sql 종료
# conn.close()