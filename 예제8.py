import tkinter as tk  # tkinter 모듈 불러오기

def show_message(msg):  # 메뉴 클릭 시 라벨에 메시지를 표시하는 함수
    label.config(text=msg)  # 라벨 텍스트 설정

root = tk.Tk()  # 루트 윈도우 생성

menu = tk.Menu(root)  # 메뉴바 생성
root.config(menu=menu)  # 루트 윈도우에 메뉴바 설정

# 파일 메뉴 생성 및 항목 추가
file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="Open", command=lambda: show_message("Open clicked"))
menu.add_cascade(label="File", menu=file_menu)  # 상위 메뉴로 'File' 추가

# 도움말 메뉴 생성 및 항목 추가
help_menu = tk.Menu(menu, tearoff=0)
help_menu.add_command(label="About", command=lambda: show_message("About clicked"))
menu.add_cascade(label="Help", menu=help_menu)  # 상위 메뉴로 'Help' 추가

label = tk.Label(root, text="")  # 메시지를 표시할 라벨 생성
label.pack()  # 라벨 배치

root.mainloop()  # 이벤트 루프 실행
