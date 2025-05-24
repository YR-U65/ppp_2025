
import random


def hangman(word, answer, alphabet):

    correct = False
    for i in range(len(word)):
        if word[i] == alphabet:
            answer[i] = word[i]
            correct = True
    return correct


def main():
    word_list = ['banana', 'mango', 'strawberry', 'apple', 'grape']
    word = random.choice(word_list)
    answer = ["_" for n in range(len(word))]
    life = 0

    while True:
        alphabet = input(f"{"".join(answer)}  입력:")
        if hangman(word, answer, alphabet) == True:
            print(f"{alphabet} 있음")
        else:
            life += 1
            print(f"{alphabet} 없음")
        if life > 4 :
            print(f"{life}회 틀리셨습니다. 게임오버.")
            break
        elif "_" not in answer:
            print(f"완성된 단어는 {word}입니다.")
            break

if __name__ == "__main__":
    main()