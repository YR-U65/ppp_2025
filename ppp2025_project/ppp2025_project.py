import pandas as pd
from datetime import datetime 
from tkcalendar import Calendar
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import koreanize_matplotlib
import os


def calendar():
    window = tk.Tk()
    window.title("Plant Diary")
    window.geometry("340x350")
    cld = Calendar(window, selectmode = "day", date_pattern = "yyyy-mm-dd", locale = "ko_KR", weekendforeground = "red" , firstweekday = "sunday", showweeknumbers = False)
    cld.grid(row = 0, column = 0, padx=70, pady=10)
    tk.Label(window, text = "작성할 개체를 선택하세요.").grid(row = 1, column=0)

    plant_var = tk.IntVar()
    plant_var.set(-1)

    p_name = ["Low1", "Low2", "Ctrl1", "Ctrl2", "High1", "High2"]

    def choose():
        idx = plant_var.get()
        if idx >= 0 :
            date = cld.get_date()
            plant_diary(date, p_name[idx])
            plant_var.set(-1)

    for i in range(6):
        rb = tk.Radiobutton(window, text=p_name[i], variable=plant_var, value=i, command=choose)
        rb.grid(row = i+2, column= 0, padx=100, sticky ='w')
        
    window.mainloop()


def plant_diary(date, nums):

    input_window = tk.Toplevel()
    input_window.title(f"{date} - {nums} 기록 입력")

    input_window.geometry("340x270")

    tk.Label(input_window, text=f"날짜: {date}").grid(row = 0, column = 1)
    tk.Label(input_window, text=f"선택: {nums}").grid(row = 1, column = 1)

    tk.Label(input_window, text="엽온(°C):").grid(row=2, column=0, pady=5, padx=5,)
    l_temp = tk.Entry(input_window)
    l_temp.grid(row=2, column=1)

    tk.Label(input_window, text="엽장(cm):").grid(row=3, column=0)
    s_length = tk.Entry(input_window)
    s_length.grid(row=3, column=1)

    tk.Label(input_window, text="엽폭(cm):").grid(row=4, column=0)
    s_width = tk.Entry(input_window)
    s_width.grid(row=4, column=1)

    tk.Label(input_window, text="생체중(g):").grid(row=5, column=0)
    fresh_weight = tk.Entry(input_window)
    fresh_weight.grid(row=5, column=1)

    tk.Label(input_window, text="기타 기록:").grid(row=6, column=0)
    notes = tk.Text(input_window, height=5, width=30)
    notes.grid(row=6, column=1)

    def on_save():
        button(date, nums, l_temp.get(), s_length.get(), s_width.get(), fresh_weight.get(), notes.get("1.0", "end").strip())

        input_window.destroy()

    tk.Button(input_window, text="저장", command= on_save).grid(row = 7, column=1)
    

def button(date, nums, l_temp, s_length, s_width, fresh_weight, notes):
    newfilename = "C:/Users/user/Desktop/청경채/청경채 생육조사/비파괴조사_청경채.csv"
    notepath = f"C:/Users/user/Desktop/청경채/청경채 생육조사/{date}_{nums}_특이사항.txt"
    if not os.path.exists(newfilename):
        df = pd.DataFrame(columns=["날짜", "개체 이름", "엽온", "엽장", "엽폭", "생체중"])
    else :
        df = pd.read_csv(newfilename)

    n_row = {"날짜": date, "개체 이름": nums, "엽온": l_temp, "엽장": s_length, "엽폭": s_width, "생체중": fresh_weight}

    df = pd.concat([df, pd.DataFrame([n_row])])
    df.to_csv(newfilename, encoding="utf-8-sig", index=False)
    if len(notes) > 0:
        with open(notepath, "a", encoding="utf-8-sig") as f:
            f.write(notes + "\n")


def graph(filename):
    df = pd.read_csv(filename, skipinitialspace = True)
    df["날짜"] = pd.to_datetime(df["날짜"], errors="coerce")
    plant_list = ["Low1", "Low2", "Ctrl1", "Ctrl2", "High1", "High2"]
    content_list = ["생체중" , "엽폭", "엽장"]
    fig, ax = plt.subplots(1, 6, figsize=(18,10))

    Low1 = df[df["개체 이름"] == "Low1"]
    Low2 = df[df["개체 이름"] == "Low2"]
    Ctrl1 = df[df["개체 이름"] == "Ctrl1"]
    Ctrl2 = df[df["개체 이름"] == "Ctrl2"]
    High1 = df[df["개체 이름"] == "High1"]
    High2 = df[df["개체 이름"] == "High2"]

    

    data_list = [Low1, Low2, Ctrl1, Ctrl2, High1, High2]

    for data in data_list:
        data = data.sort_values("날짜")

    for i in range(6):
        ax[i].plot(data_list[i]["날짜"], data_list[i]["생체중"], color = "blue")
        ax[i].set_title(plant_list[i])
        ax[i].set_xlabel("날짜")
        ax[i].set_ylabel("생체중(g)")
        ax[i].grid(True)

    min_w = df["생체중"].min()
    max_w = df["생체중"].max()
    
    df["날짜"] = pd.to_datetime(df["날짜"])
    start_d = df["날짜"].min()
    end_d = df["날짜"].max()

    for a in ax:
        a.set_xlim(start_d, end_d)
        a.set_ylim(min_w, max_w)
        a.xaxis.set_major_locator(mdates.DayLocator(interval=2))
        a.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d')) 
        a.tick_params(axis='x', rotation=45)

    fig.subplots_adjust(hspace=0.5)
    

    return plt.show()


def main():
    calendar()
    filename = "C:/Users/user/Desktop/청경채/청경채 생육조사/비파괴조사_청경채.csv"
    graph(filename)


if __name__ == "__main__":
    main()