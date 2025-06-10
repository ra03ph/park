import tkinter as tk  # tkinter 모듈을 불러옴

# 버튼 클릭 시 실행될 함수 정의
def greet():
    name = entry.get()  # 입력창에서 텍스트(이름)를 가져옴
    label.config(text=f'Hello, {name}!')  # Label의 텍스트를 'Hello, [이름]!'으로 변경

# 기본 GUI 창 생성
root = tk.Tk()  # 최상위 윈도우 생성

entry = tk.Entry(root)  # 이름을 입력받을 입력창 생성
entry.pack()  # 입력창을 화면에 배치

# 버튼 위젯 생성 (텍스트는 "Greet", 클릭 시 greet 함수 실행)
button = tk.Button(root, text="Greet", command=greet)
button.pack()  # 버튼을 화면에 배치

label = tk.Label(root, text="")  # 인사말을 표시할 라벨 생성 (초기에는 빈 문자열)
label.pack()  # 라벨을 화면에 배치

root.mainloop()  # GUI 이벤트 루프 시작
