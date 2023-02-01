"""
1) 화면상에 메뉴를 출력함 (종료를 선택할 때까지 반복, while문 사용)
    - 1. 블랙커피, 2: 프림커피, 3: 설탕프림 커피, 4: 재고현황, 5: 종료
    - 커피 가격은 모두 300원으로 동일함

2) 초기 자판기 상황
    - 자판기 동전: 10,000원 (모두 100원짜리 100개 보유)
    - 물: 1000ml
    - 커피: 500g, 프림: 500g, 설탕: 500g, 종이컵 30개

3) 메뉴에 따른 커피, 설탕, 프림 소모량
    - 블랙커피: 커피 30g + 물 100ml
    - 프림커피: 커피 15g + 프림 15g + 물 100ml
    - 설탕커피: 커피 10g + 프림 10g + 설탕 10g + 물 100ml

4) 재고현황
    - 커피 재고량, 프림 재고량, 설탕 재고량, 컵 재고량, 잔여 물용량 출력
    - 잔돈 현황 출력 (입출금 관리)
"""
# def use(button):
#     if button == '1':
#         coffee -= 30
#         water -= 100
#         machine += 300
#         cup -= 1
#     elif button == '2':
#         coffee -= 15
#         creamer -= 15
#         water -= 100
#         machine += 300
#         cup -= 1
#     elif button == '3':
#         coffee -= 15
#         creamer -= 15
#         sugar -= 10
#         water -= 100
#         machine += 300
#         cup -= 1

def inven(coffee, creamer, sugar, water, cup, machine, money):
    print(f"재고현황:\n커피: {coffee}g, 프림: {creamer}g, 설탕: {sugar}g")
    print(f"물: {water}ml, 종이컵: {cup}개")
    print(f"자판기 남은 돈: {machine}원, 잔돈 현황: {money}원")

def menu():
    print(" "*8 + "커피 자판기 (300원)" + " "*8)
    print(f"1: 블랙커피\n2: 프림커피\n3: 설탕프림 커피\n4: 재고현황\n5: 종료")



def vendingmachine():
    water, coffee, creamer, sugar, cup = 1000, 500, 500, 500, 30
    machine = 10000

    coin = int(input("동전을 투입하세요: ").strip())
    if coin < 300:
        print(f"돈이 부족합니다 {coin}원:")
        print(f'{"-"*30}\n커피 자판기 동작을 종료합니다.\n{"-"*30}')
    else:
        while True:
            menu()
            button = input("메뉴를 선택하세요 : ").strip()

            if button == '1':
                coin -= 300
                if coin < 300:
                    print(f"블랙 커피를 선택하셨습니다. 잔돈: {coin}")
                    print("잔돈이 부족해서 종료합니다.")
                    break
                else:
                    coffee -= 30
                    water -= 100
                    machine += 300
                    cup -= 1
                    print(f"블랙 커피를 선택하셨습니다. 잔돈: {coin}")
            
            elif button == '2':
                coin -= 300
                if coin < 300:
                    print(f"프림 커피를 선택하셨습니다. 잔돈: {coin}")
                    print("잔돈이 부족해서 종료합니다.")
                    break
                else:
                    coffee -= 30
                    creamer -= 15
                    water -= 100
                    machine += 300
                    cup -= 1
                    print(f"프림 커피를 선택하셨습니다. 잔돈: {coin}")

            elif button == '3':
                coin -= 300
                if coin < 300:
                    print(f"설탕 프림 커피를 선택하셨습니다. 잔돈: {coin}")
                    print("잔돈이 부족해서 종료합니다.")
                    break
                else:
                    coffee -= 30
                    creamer -= 15
                    sugar -= 10
                    water -= 100
                    machine += 300
                    cup -= 1
                    print(f"설탕 프림 커피를 선택하셨습니다. 잔돈: {coin}")

            elif button == '4':
                inven(coffee, creamer, sugar, water, cup, machine, coin)
            
            elif button == '5':
                print("커피 자판기 동작을 종료합니다.")
                break

vendingmachine()