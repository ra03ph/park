import tkinter as tk  # tkinter 모듈 불러오기

# 색상을 변경하는 함수
def change_color():
    root.configure(bg=color.get())  # 선택된 색상으로 배경색 설정

root = tk.Tk()  # GUI 창 생성

color = tk.StringVar()  # 라디오 버튼의 선택값을 저장할 변수

# 세 개의 라디오 버튼 생성: 빨강, 파랑, 초록
tk.Radiobutton(root, text="Red", variable=color, value="red", command=change_color).pack()
tk.Radiobutton(root, text="Blue", variable=color, value="blue", command=change_color).pack()
tk.Radiobutton(root, text="Green", variable=color, value="green", command=change_color).pack()

root.mainloop()  # 이벤트 루프 실행
