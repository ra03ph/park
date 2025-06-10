import tkinter as tk  # tkinter 모듈을 불러옴 (tk는 별칭)

# 버튼 클릭 시 실행될 함수 정의
def say_hello():
    label.config(text="Hello, World!")  # Label의 텍스트를 "Hello, World!"로 변경

# 기본 GUI 창 생성
root = tk.Tk()  # 최상위 윈도우 생성

# 버튼 위젯 생성 (텍스트는 "Click Me", 클릭 시 say_hello 함수 실행)
button = tk.Button(root, text="Click Me", command=say_hello)
button.pack()  # 버튼을 화면에 배치

# 라벨 위젯 생성 (초기 텍스트는 빈 문자열)
label = tk.Label(root, text="")
label.pack()  # 라벨을 화면에 배치

# GUI 이벤트 루프 시작
root.mainloop()
