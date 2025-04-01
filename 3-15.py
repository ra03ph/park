class FuelTank:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_fuel = capacity

    def display_status(self):
        print(f"현재 탱크의 연료는 {self.current_fuel}입니다.")

    def adjust_fuel(self, adjustment):
        self.current_fuel += adjustment
        if self.current_fuel < 0:
            self.current_fuel = 0
        
        self.display_status()
        
        # 10% 미만 경고
        if self.current_fuel < self.capacity * 0.1:
            print("경고: 연료가 10% 미만입니다. 충전하세요!")

# 초기 연료 양
fuel_tank = FuelTank(500)

# 사용자 입력 처리
while True:
    user_input = input("충전 또는 사용한 연료를 입력하세요 (+/- 기호와 함께 입력하세요): ")
    if user_input.lower() == 'exit':
        break
    try:
        adjustment = int(user_input)
        fuel_tank.adjust_fuel(adjustment)
    except ValueError:
        print("잘못된 입력입니다. 숫자와 + 또는 - 기호를 입력하세요.")
