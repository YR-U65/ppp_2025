import random
import rich
from rich.console import Console
from rich.table import Table

console = Console()

def gugudan():
    
    num1 = random.randint(2, 9)
    num2 = random. randint(1, 9)
    gugu = num1*num2

    while True:
        is_correct = False
        try:
            answer = int(input(f"{num1} * {num2} = "))
            break

        except ValueError:
                print("다시 입력해주세요")
                
    if gugu == answer :
        is_correct = True
    else:
        is_correct = False
    return num1, num2, answer, gugu, is_correct

def main():
    table = Table(show_header = True, header_style = "bold magenta")
    
    n = 5
    count = 0
    correct = 0
    correct_answer = "오답"

    table.add_column("문제", justify = "center")
    table.add_column("답", justify = 'center')
    table.add_column("정답/오답", justify = "center")
    table.add_column("맞힌 횟수", justify = "center")
    console.print(table)

    while count < n:
        num1, num2, answer, gugu, is_correct = gugudan()
        if is_correct == True:
            correct_answer = "정답"
            correct += 1
        else:
            correct_answer = "오답"
        table.add_row(f"{num1} * {num2}", str(answer), correct_answer, str(correct))
        count += 1

        console.clear()
        console.print(table)

    console.print(f"{n}문제 중 {correct}개 맞추셨습니다. {correct/count * 100: .0f}점 입니다.")

    
if __name__ == "__main__":
    main()