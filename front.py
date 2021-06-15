
from tkinter import *
import tkinter

window=tkinter.Tk()

window.title("New Movie Rangking")
window.geometry("640x400+100+100")
window.resizable(False,False)

title=tkinter.Label(window,text="Pop Corn Movie", anchor=CENTER)
title.pack() # 위젯을 배치

lbl = Label(window, text="PCM")
lbl.grid(row=0,column=0)
 
txt = Entry(window)
 
btn = Button(window, text="Let's go!",width=30,height=5)
btn.grid(row=220,column=200)
#btn.pack() 불필요한 공간 없앤다
 
window.mainloop()
