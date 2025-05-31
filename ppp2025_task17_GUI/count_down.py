import time
import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(text):
    return simpledialog.askstring(title = "카운트다운" , prompt= text)


def countdown(n, label):
    if n>=0:
        for i in range(n, 0, -1):
            label.config(text=str(i))
            label.update()
            time.sleep(1)
    else:
        label.config(text = "Bomb!")
    label.config(text = "Bomb!")
    label.update()



def main():
   n = int(gui_input("몇 초 셀까요?"))
   countdown_window = tk.Tk()
   countdown_window.title("카운트다운")
   countdown_window.geometry("30x50+750+400")
   label=tk.Label(countdown_window, text = "", font=("Arial", 15))
   label.pack(expand=True)

   countdown(n, label)
   countdown_window.mainloop()

if __name__ == "__main__":
    main()