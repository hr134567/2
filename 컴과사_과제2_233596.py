# 주차타워
parking_tower = []
def tower_input() :
    while True :
        car_number = input("입고할 차량번호 뒷자리를 입력하세요 : ")
        if len(car_number) == 4 :
            print(f"{car_number} 차량이 입고되었습니다.")
            break
        else :
            print("4자리를 입력하세요.")
    if len(parking_tower) == 5 :
        print("더 이상 차량을 입고할 수 없습니다.(최대 : 5대 / 현재 : 5대")
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

tower_input()
tower_output()
print(parking_tower)
