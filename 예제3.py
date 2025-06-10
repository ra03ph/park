import tkinter as tk  # tkinter 모듈 불러오기

# 더하기 함수 정의
def add():
    result = int(entry1.get()) + int(entry2.get())  # 두 입력창의 값을 정수로 변환 후 더함
    label.config(text=f"Result: {result}")  # 결과를 라벨에 출력

root = tk.Tk()  # GUI 창 생성

entry1 = tk.Entry(root)  # 첫 번째 입력창 생성
entry1.pack()  # 입력창 배치

entry2 = tk.Entry(root)  # 두 번째 입력창 생성
entry2.pack()  # 입력창 배치

# "Add" 버튼 생성, 클릭 시 add 함수 실행
button = tk.Button(root, text="Add", command=add)
button.pack()  # 버튼 배치

label = tk.Label(root, text="")  # 결과 출력용 라벨 생성 (초기 텍스트 없음)
label.pack()  # 라벨 배치

root.mainloop()  # 이벤트 루프 실행
