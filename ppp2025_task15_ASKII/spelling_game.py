
import random


change2it = lambda ch: (ord(ch) - ord("가")) // 588


def initial_change(ch):
    text = []
    initial = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
    for txt in ch:
        text.append(initial[change2it(txt)])
    return "".join(text)


def main():
    
    solution = ["바나나" , "사과" , "복숭아", "포도", "망고", "수박"]
    question = random.choice(solution)
    count = 0
    while True:
        answer = input(f"{initial_change(question)}(과일) : ")
        if answer in solution:
            print("정답입니다.")
            break
        else:
            count += 1
            print("오답입니다.")
            if count > 2 :
                print(f"{count}회 시도하셨습니다. 게임 오버.")
                break

if __name__ == "__main__":
    main()
