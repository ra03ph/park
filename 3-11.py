def calculate_days_to_escape(depth, climb, slip):
    day = 0
    position = 0

    while position < depth:
        day += 1
        position += climb
        print(f"day: {day}\t달팽이의 위치: {position} 미터")

        if position >= depth:
            break
        
        position -= slip

    print(f"\n달팽이가 탈출하는 데 걸린 날 수: {day}일")
    return day

# 깊이 30미터, 낮에 7미터 올라가고 밤에 5미터 미끄러짐
calculate_days_to_escape(30, 7, 5)
