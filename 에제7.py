import tkinter as tk  # tkinter 모듈 불러오기

def show_fruit(event):  # Listbox 선택 이벤트 처리 함수
    selection = listbox.get(listbox.curselection())  # 선택한 항목 가져오기
    label.config(text=f"Selected: {selection}")  # 라벨에 선택한 항목 표시

root = tk.Tk()  # 루트 윈도우 생성

listbox = tk.Listbox(root)  # 리스트박스 위젯 생성
# 리스트박스에 항목 추가
for fruit in ["Apple", "Banana", "Cherry"]:
    listbox.insert(tk.END, fruit)
listbox.pack()  # 리스트박스 배치

listbox.bind("<<ListboxSelect>>", show_fruit)  # 항목 선택 이벤트 바인딩

label = tk.Label(root, text="")  # 결과 출력용 라벨 생성
label.pack()  # 라벨 배치

root.mainloop()  # 이벤트 루프 실행
