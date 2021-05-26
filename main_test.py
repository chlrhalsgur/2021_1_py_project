import crawling_test3 as crw
import db_test1
import Rerating_movie

crw.crawling_movie()
movie_list = db_test1.print_db() 
rerated_movie = Rerating_movie.rerate(movie_list) # test 안 해봄
