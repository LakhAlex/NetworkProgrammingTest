from tkinter import *
root = Tk()

'''
# 1. 윈도우 창 특성 변경
root.title("opt window") # 창 이름 변경
root.geometry("300x100+300+300") # 창 크기 + 창의 좌표
root.resizable(False, False) # 창 크기 변경 허용 여부

# 2. Label window
label = Label(root, text="Hello TKINTER") # Label 생성
label.pack() # 레이블을 화면에 배치
'''

'''
# 3. Button window - 창에 버튼/이벤트 추가
count = 0
def count_plus():
    global count
    count += 1
    label.config(text=str(count))

def count_minus():
    global count
    count -= 1
    label.config(text=str(count))
label = Label(root, text="0") # Label 생성
label.pack()

# 버튼 생성
btn1 = Button(root, width=10, text="plus", overrelief="solid", command=count_plus)
btn1.pack()
btn2 = Button(root, width=10, text="minus", overrelief="solid", command=count_minus)
btn2.pack()
'''

# 4. entry window - 창에 입력창 추가
def calc(event):
    label.config(text="계산결과 : " + str(eval(entry.get())))

label = Label(root, text="0")  # Label 생성
label.pack()

entry = Entry(root, width=30) # Entry 생성
entry.bind("<Return>", calc) # Entry 이벤트 부여
entry.pack() # 엔트리 화면에 배치

root.mainloop() # TK 화면 출력