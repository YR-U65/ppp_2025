

import random

def gugudan():
    
    num1 = random.randint(2, 9)
    num2 = random. randint(1, 9)
    gugu = num1*num2

    while True:
        try:
            answer = int(input(f"{num1} * {num2} = "))
            break

        except ValueError:
                print("다시 입력해주세요")
                
    if gugu == answer :
        return True
    else:
        return False

def main():
    n = 5
    count = 0
    correct = 0
    while count < n:
        if gugudan() == True:
            print("정답")
            correct += 1
        else:
            print("오답")
        count += 1
    print(f"{n}문제 중 {correct}개 맞추셨습니다. {correct/count * 100: .0f}점 입니다.")

if __name__ == "__main__":
    main()