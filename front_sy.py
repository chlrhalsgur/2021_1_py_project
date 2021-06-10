from tkinter import *
#from tkhtmlview import HTMLLabel  //html사용해서 네이버영화, 네이버영화랭킹링크 사용할려고 했음 but 안됨
#https://remixicon.com/    사용할려고 했던 아이콘

win=Tk()

#Show Movie 클릭했을 경우
def Naver_movie_Ranking():
    window_naver=Toplevel(win)
    window_naver.geometry("1000x600")



#두 번째 페이지
def create_window():
    window = Toplevel(win) #새로운 창 열기
    window.geometry("1000x600")
    window.configure(bg='#4682B4')
    btn = Button(window, text = "Show Movie", command=Naver_movie_Ranking)
    btn1 = Button(window, text = "Show Movie Ranking")
    btn2 = Button(window, text = "Our New Movie Ranking")

    btn.pack(pady=40)
    btn1.pack(pady=20)
    btn2.pack(pady=20)



win.geometry("1000x600")  #사이즈 가로x세로(픽셀)
win.title("Movie Ranking") #타이틀
win.option_add("*Font","Courier 40") #기본 폰트와 글자크기 설정

#첫 번째 페이지
lab=Label(win, text = "Pop Corn Movie")
lab.pack(side=TOP, pady=60)
lab.configure(font=("Courier", 70, "italic"))

#첫 번째 페이지 버튼
btn = Button(win, text="Let's start", command=create_window)
btn.pack(side=BOTTOM, pady=50)

 #배경색
win.configure(bg='#49A')




win.mainloop() #창 열기
