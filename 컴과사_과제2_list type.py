# 주차타워
def tower_input() :
    global count
    if count == 5 :
        print("→ 더 이상 차량을 입고할 수 없습니다.(최대 : 5대 / 현재 : 5대)")
    else :
        while True :
            print("-" * 30)
            car_number = int(input("입고할 차량번호 뒷자리를 입력하세요 : "))
            if 1000 <= car_number <= 9999 :
                if car_number in parking_tower:
                    print("→ 이미 입고되어 있습니다.")
                    break
                else:
                    for i in range(5) :
                        if parking_tower[i] == '' :
                            parking_tower[i] = car_number
                            count += 1
                            print(f"→ {car_number} 차량이 입고되었습니다.")
                            return
            else:
                print("→ 4자리를 입력하세요.")
def tower_output() :
    global count
    while True :
        print("-" * 30)
        car_number = int(input("출고할 차량번호 뒷자리를 입력하세요 : "))
        if 1000 <= car_number <= 9999 :
            break
        else :
            print("→ 4자리를 입력하세요.")
    if car_number in parking_tower :
        car_number_index = parking_tower.index(car_number)
        parking_tower[car_number_index] = ''
        count -= 1
        print(f"→ {car_number} 차량이 출고되었습니다.")
    else :
        print(f"→ {car_number} 차량이 존재하지 않습니다.")
def tower_information() :
    for i, car_number in enumerate(parking_tower) :
        print(f"{i+1}층 : {car_number}")
def tower_exit() :
    print("→ 프로그램을 종료합니다.")
    exit()
def tower_menu() :
    print("-" * 30)
    print("1. 차량입고")
    print("2. 차량출고")
    print("3. 차량입고정보")
    print("4. 프로그램 종료")
    print("-" * 30)

parking_tower = ['','','','','']
count = 0
while True :
    tower_menu()
    while True :
        menu_number = int(input("기능을 선택해주세요(1~4) : "))
        if 1 <= menu_number <= 4 :
            break
        else :
            print("→ 1에서 4의 값만 입력해주세요.")
            print("-" * 30)
    if menu_number == 1 :
        tower_input()
    elif menu_number == 2 :
        tower_output()
    elif menu_number == 3 :
        tower_information()
    else :
        tower_exit()
