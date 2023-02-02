class tennis:
    def select(self):
        print("-"*30)
        print("1. 테니스 공 넣기")
        print("2. 테니스 공 꺼내기")
        print("3. 테니스 공 개수 출력")
        print("4. 종료")
        print("-"*30)
        self.menu = int(input("메뉴를 선택하세요: "))

        if self.menu == 4:
            return
        else:
            if self.menu == 1:
                return self.push()
            elif self.menu == 2:
                return self.pop()
            elif self.menu == 3:
                return self.count()
            else:
                print("잘못된 메뉴 선택입니다.")
                return self.select()

    def __init__(self):
        self.ball = 0
        self.ballList = []
        return self.select()
    
    def push(self):
        if len(self.ballList) < 5:
            self.ball += 1
            self.ballList.append(str(self.ball))
            self.count()
        else:
            print("케이스가 꽉 찼습니다.")
            return self.select()
        
    def pop(self):
        if len(self.ballList) > 1:
            self.ball -= 1
            print(f"Pop({self.ballList[-1]})")
            del (self.ballList)[-1]
            self.count()
        else: 
            print(f"Pop({self.ballList[-1]})")
            del (self.ballList)[-1]
            print("케이스가 비어있습니다.")
            self.ball = 0
            return self.select()

    def count(self):
        if len(self.ballList) > 0:
            print(f"[공의 개수]: {len(self.ballList)}")
            print(' '.join(sorted(self.ballList, reverse=True)))
        else:
            print("케이스가 비어 있습니다.")
        
        return self.select()
        
tennis()


class Stack:
    def __init__(self, stack_size):
        self.stack = [] * stack_size
        self.max_stack_size = stack_size
        self.top = -1
        self.coin_count = 1

    def push(self):
        if (self.top < self.max_stack_size):
            self.top += 1
            self.stack.append(self.coin_count)
            self.show_stack()
        else:
            print('Stack is full')

    def pop(self):
        if (self.top > 0):
            item = self.stack[self.top]
            print('Pop(', item, ')')
            self.top -= 1
            self.show_stack()
        else:
            print('Stack is empty')

    def show_stack(self):
        if (self.top < 0):
            print('Stack is empty. No item in stack')
            return
        
        print('[Stack size]: ', self.top + 1)
        for index in range(self.top, -1, -1):
            print(self.stack[index], end='')
        print()

def show_menu():
    print("-"*30)
    print("1. 테니스 공 넣기")
    print("2. 테니스 공 꺼내기")
    print("3. 테니스 공 개수 출력")
    print("4. 종료")
    print("-"*30)
    opt = int(input("메뉴를 선택하세요: "))
    return opt