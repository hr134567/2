# 주차타워
def tower_input() :
    while True :
        car_number = input("입고할 차량번호 뒷자리를 입력하세요 : ")
        if len(car_number) == 4 :
            print(f"{car_number} 차량이 입고되었습니다.")
            break
        else :
            print("4자리를 입력하세요.")
    if len(parking_tower) == 5 :
        print("더 이상 차량을 입고할 수 없습니다.(최대 : 5대 / 현재 : 5대)")
    else :
        parking_tower.append(car_number)
def tower_output() :
    while True :
        car_number = input("출고할 차량번호 뒷자리를 입력하세요 : ")
        if len(car_number) == 4 :
            break
        else :
            print("4자리를 입력하세요.")
    if car_number in parking_tower :
        parking_tower.remove(car_number)
        print(f"{car_number} 차량이 출고되었습니다.")
    else :
        print(f"{car_number} 차량이 존재하지 않습니다.")
def tower_information() :
    if len(parking_tower) == 0 :
        print("현재 입고된 차량이 없습니다.")
    else :
        for i, car_number in enumerate(parking_tower) :
            print(f"{i+1}층 : {car_number}")
def tower_exit() :
    print("프로그램을 종료합니다.")
    exit()
def tower_menu() :
    print("●" * 30)
    print("1. 차량입고")
    print("2. 차량출고")
    print("3. 차량입고정보")
    print("4. 프로그램 종료")
    print("●" * 30)

parking_tower = []
while True :
    tower_menu()
    while True :
        menu_number = int(input("기능을 선택해주세요(1~4) : "))
        if 1 <= menu_number <= 4 :
            break
        else :
            print("1에서 4의 값만 입력해주세요.")
    if menu_number == 1 :
        tower_input()
    elif menu_number == 2 :
        tower_output()
    elif menu_number == 3 :
        tower_information()
    else :
        tower_exit()


