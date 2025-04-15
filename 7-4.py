print("사전 프로그램 시작... 종료는 q를 입력")

while True:
    cmd = input("$ ").strip()

    if cmd == 'q':
        print("사전 프로그램을 종료합니다.")
        break

    if cmd.startswith("<"):
        try:
            word_pair = cmd[1:].strip()
            eng, kor = word_pair.split(":")
            dictionary[eng.strip()] = kor.strip()
        except:
            print("입력오류가 발생했습니다.")
    elif cmd.startswith(">"):
        eng = cmd[1:].strip()
        if eng in dictionary:
            print(dictionary[eng])
        else:
            print(f"{eng}가 사전에 없습니다.")
    else:
        print("입력오류가 발생했습니다.")
