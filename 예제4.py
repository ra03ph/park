import tkinter as tk  # tkinter 모듈 불러오기

# 선택된 항목을 확인하는 함수
def show_selection():
    selections = []  # 선택된 항목을 저장할 리스트
    if var1.get():  # 첫 번째 체크박스가 선택되었는지 확인
        selections.append("Option 1")
    if var2.get():  # 두 번째 체크박스가 선택되었는지 확인
        selections.append("Option 2")
    label.config(text=", ".join(selections))  # 선택된 항목을 라벨에 표시

root = tk.Tk()  # GUI 창 생성

var1 = tk.BooleanVar()  # 체크 상태를 저장할 변수 1
var2 = tk.BooleanVar()  # 체크 상태를 저장할 변수 2

# 두 개의 체크박스 생성 및 배치
tk.Checkbutton(root, text="Option 1", variable=var1).pack()
tk.Checkbutton(root, text="Option 2", variable=var2).pack()

# "Show" 버튼 클릭 시 선택 결과 표시
tk.Button(root, text="Show", command=show_selection).pack()

label = tk.Label(root, text="")  # 결과 출력용 라벨 생성
label.pack()  # 라벨 배치

root.mainloop()  # 이벤트 루프 실행
