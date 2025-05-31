
import random
import rich
from rich.console import Console
from rich.table import Table
from rich.live import Live


def hangman(word, answer, alphabet):

    correct = False
    for i in range(len(word)):
        if word[i] == alphabet:
            answer[i] = word[i]
            correct = True
    return correct

def render_table(answer, life, guessed, message):
    table = Table(show_header=True, header_style="bold red")
    table.add_column("행 맨 : 과일", justify="center")
    table.add_row(f"[bold red]♥[/bold red]" * life)
    table.add_row(" ".join(answer))
    table.add_row("입력한 글자: " + " ".join(guessed))
    table.add_row(f"[bold]{message}[/bold]")
    return table


def main():
    word_list = ['banana', 'mango', 'strawberry', 'apple', 'grape']
    word = random.choice(word_list)
    answer = ["_" for n in range(len(word))]
    life = 5
    guessed = []
    message = ""
    console = Console()

    with Live(render_table(answer, life, guessed,message), refresh_per_second=4) as live:
        while True:
            alphabet = console.input("한 글자의 알파벳을 입력하세요: ").lower()
            guessed.append(alphabet)

            if hangman(word, answer, alphabet):
                message = f"[green]{alphabet} 있음.[/green]"
            else:
                life -= 1
                message = f"[red]{alphabet} 없음.[/red]"
                if life == 0:
                    message = f"[bold red]게임 오버! 정답은 {word}입니다.[/bold red]"
                    live.update(render_table(answer, life, guessed, message))
                    break

            live.update(render_table(answer, life, guessed, message))

if __name__ == "__main__":
    main()