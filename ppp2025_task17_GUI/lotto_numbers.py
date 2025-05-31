
import random
import tkinter as tk



def lotto():
    lotto_nums = []
    while len(lotto_nums) < 6:
            num = random.randint(1, 45)
            if num not in lotto_nums:
                lotto_nums.append(num)
    lotto.label.config(text=" ".join(map(str, lotto_nums)))




def main():
    win_lotto = tk.Tk()
    win_lotto.title("로또 번호 추첨")
    win_lotto.geometry("300x100+750+400")
    label = tk.Label(win_lotto, width=15, height=2,text = "추첨하세요.", font=("Arial", 15))
    label.pack()
    lotto.label = label
    button = tk.Button(win_lotto, text = "로또 번호 추첨", width=15, height=1, command= lotto, font=("Arial", 13))
    label.pack()
    button.pack()
    win_lotto.mainloop()

    




if __name__ == "__main__":
    main()