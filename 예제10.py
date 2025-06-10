import tkinter as tk  # tkinter 모듈 임포트
import time  # 시간 관련 함수 사용을 위한 모듈 임포트

# 시간을 갱신하는 함수 정의
def update_time():
    # 현재 시간을 문자열 형식으로 가져옴 (시:분:초)
    current = time.strftime("%H:%M:%S")
    label.config(text=current)  # 라벨에 현재 시간 표시
    root.after(1000, update_time)  # 1000밀리초(1초) 후 다시 이 함수를 호출

# tkinter 윈도우 생성
root = tk.Tk()

# 시간 표시용 라벨 생성 (Arial 폰트, 크기 24)
label = tk.Label(root, font=("Arial", 24))
label.pack()  # 라벨 화면에 배치

update_time()  # 처음 시간 표시 시작
root.mainloop()  # 이벤트 루프 시작
