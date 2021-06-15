# Treeview 메서드는 tkinter의 ttk 모듈 내부에 존재한다. tkinter.ttk 모듈로 호출한다.
import tkinter
import tkinter.ttk

# 표에 삽입될 데이터
treelist=[
    ["Tom", 80, 3], 
    ["Bani", 71, 5], 
    ["Boni", 90, 2], 
    ["Dannel", 78, 4], 
    ["Minho", 93, 1]
]
MOVIE = [
    ['홀리데이', '8.67', 16],
    ['화차', '8.3018', 13],
    ['화차', '8.3018', 13],
    ['환생', '8.181', 2],
    ['후크', '9.12', 12],
    ['휴고', '7.78', 12],
    ['히든 페이스', '8.291500000000001', 7],
    ['히든 피겨스', '9.182599999999999', 1],
    ['히트', '9.11', 16]
]

def make_table():
    # GUI창을 생성하고 라벨을 설정한다.
    root=tkinter.Tk()
    root.title("Students")
    root.geometry("540x300+100+100")
    root.resizable(False, False)

    lbl = tkinter.Label(root, text="Movie Ranking") # 제목
    lbl.pack() 

    # 표 생성하기. colums는 컬럼 이름, displaycolums는 실행될 때 보여지는 순서다.
    treeview=tkinter.ttk.Treeview(root, columns=["one", "two","three"], displaycolumns=["one","two","three"])
    treeview.pack()

    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("#0", width=100,)
    treeview.heading("#0", text="index")

    treeview.column("#1", width=100, anchor="center")
    treeview.heading("one", text="Title", anchor="center")

    treeview.column("#2", width=100, anchor="center")
    treeview.heading("two", text="Rate", anchor="center")

    treeview.column("#3", width=70, anchor="center")
    treeview.heading("three", text="Genre_code", anchor="center")


    # 표에 데이터 삽입
    for i in range(len(MOVIE)):
        treeview.insert('', 'end', text=i, values=MOVIE[i], iid=str(i)+"번")

    # GUI 실행
    root.mainloop()

make_table()



    # # 슴겨진 항목
    # top=treeview.insert('', 'end', text="hidden index", iid="5번")
    # top_mid1=treeview.insert(top, 'end', text="5", values=["Timy", 0, 8], iid="5번-1")
    # top_mid2=treeview.insert(top, 0, text="6", values=["Ann", 35, 7], iid="5번-0")
    # top_mid3=treeview.insert(top, 'end', text="7", values=["Sany", 60, 6], iid="5번-2")