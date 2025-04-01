def 메뉴_주문():
    print("맛난 식당에 오신 것을 환영합니다.")
    print("메뉴는 다음과 같습니다.")
    print("1. 햄버거 (b)")
    print("2. 치킨 (c)")
    print("3. 피자 (p)")

    while True:
        메뉴 = input("메뉴를 선택하세요 (알파벳 b, c, p 입력): ")

        if 메뉴 == 'b':
            print("햄버거를 선택하셨습니다.")
            break
        elif 메뉴 == 'c':
            print("치킨을 선택하셨습니다.")
            break
        elif 메뉴 == 'p':
            print("피자를 선택하셨습니다.")
            break
        else:
            print("메뉴를 다시 입력하세요.")
