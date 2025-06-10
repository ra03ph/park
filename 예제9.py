import tkinter as tk  # tkinter 모듈을 불러옴 (GUI 만들기용)

# 텍스트를 파일로 저장하는 함수 정의
def save_file():
    # "note.txt" 파일을 쓰기 모드로 열기
    with open("note.txt", "w") as f:
        # Text 위젯에서 모든 텍스트를 가져와 파일에 쓰기 (1.0: 시작, END: 끝까지)
        f.write(text.get("1.0", tk.END))

# tkinter 윈도우 생성
root = tk.Tk()

# 텍스트 입력을 위한 Text 위젯 생성
text = tk.Text(root)
text.pack()  # Text 위젯 화면에 배치

# 저장 버튼 생성 (누르면 save_file 함수 실행)
button = tk.Button(root, text="Save", command=save_file)
button.pack()  # 버튼을 화면에 배치

root.mainloop()  # 이벤트 루프 시작 (창을 닫을 때까지 프로그램 유지)
