from tkinter import *

# 창 열기 위한 객체 생성 (mainloop와 짝을 이룸)
root = Tk()
root.title("000's movie ranking") # 상단바 title
root.geometry('640x480')
# root.resizable(False,False) # 너비 높이 변경 불가 필요시 적용

btn1 = Button(root, width=10, height=3, padx=5, pady=10, fg = 'red', bg='yellow', text='btn1', command=print('click')) # 버튼 생성 (창선택, size, padding, style, text, command)
# photo = PhotoImage(file="")  # 이미지 버튼 생성
# btn2 = Button(root, image = photo)
btn1.pack() # 버튼 적용

label1 = Label(root, text="lb1")



root.mainloop()