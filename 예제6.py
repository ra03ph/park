import tkinter as tk  # tkinter 모듈을 불러옴

def resize(val):  # 슬라이더 값이 바뀔 때 실행될 함수 정의
    label.config(font=("Arial", int(val)))  # 라벨의 글꼴 크기를 슬라이더 값으로 설정

root = tk.Tk()  # 루트 윈도우 생성

# 가로 방향 슬라이더 생성, 값이 바뀌면 resize 함수 호출
scale = tk.Scale(root, from_=10, to=40, orient="horizontal", command=resize)
scale.pack()  # 슬라이더 배치

label = tk.Label(root, text="Resizable Text")  # 초기 텍스트가 있는 라벨 생성
label.pack()  # 라벨 배치

root.mainloop()  # 이벤트 루프 실행
