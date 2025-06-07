import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import requests
import os

def download_data(place, year, filename):
    URL = f"https://api.taegon.kr/stations/{place}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        req = requests.get(URL)
        req.encoding = "UTF-8"
        f.write(req.text)

def make_data():
    files = {}
    dfs = {}
    df_list = []

    for year in range(1980, 2025):
        files[year] = f"weather_146_{year}.csv"
        download_data(146, year, files[year])
        dfs[year] = pd.read_csv(files[year], skipinitialspace = True)
        dfs[year]["date"] = pd.to_datetime(dfs[year][["year", "month", "day"]])
        df_list.append(dfs[year])
    
    df_all = pd.concat(df_list, ignore_index=True)
    df_all = df_all.sort_values("date")
    df_all.to_csv("weather_146_1980_2024.csv")


def month_graph(filename):
    df = pd.read_csv(filename, skipinitialspace = True)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    summer6_df = df[df["month"]== 6]
    summer7_df = df[df["month"] == 7]
    summer8_df = df[df["month"] == 8]

    winter12_df = df[df["month"]== 12]
    winter1_df = df[df["month"]== 1]
    winter2_df = df[df["month"]== 2]
    
    fig, ax = plt.subplots(2, 3, figsize=(18,10))

    ax[0,0].plot(summer6_df["date"], summer6_df["tavg"], color = "skyblue")
    ax[0,0].set_title("June temperature")
    ax[0,0].set_xlabel("Date")
    ax[0,0].set_ylabel("tavg(℃)")
    ax[0,0].grid(True)

    ax[0,1].plot(summer7_df["date"], summer7_df["tavg"], color = "yellow")
    ax[0,1].set_title("July temperature")
    ax[0,1].set_xlabel("Date")
    ax[0,1].set_ylabel("tavg(℃)")
    ax[0,1].grid(True)

    ax[0,2].plot(summer8_df["date"], summer8_df["tavg"], color = "pink")
    ax[0,2].set_title("August temperature")
    ax[0,2].set_xlabel("Date")
    ax[0,2].set_ylabel("tavg(℃)")
    ax[0,2].grid(True)

    ax[1,0].plot(winter12_df["date"], winter12_df["tavg"], color = "blue")
    ax[1,0].set_title("December temperature")
    ax[1,0].set_xlabel("Date")
    ax[1,0].set_ylabel("tavg(℃)")
    ax[1,0].grid(True)

    ax[1,1].plot(winter1_df["date"], winter1_df["tavg"], color = "orange")
    ax[1,1].set_title("January temperature")
    ax[1,1].set_xlabel("Date")
    ax[1,1].set_ylabel("tavg(℃)")
    ax[1,1].grid(True)

    ax[1,2].plot(winter2_df["date"], winter2_df["tavg"], color = "red")
    ax[1,2].set_title("February temperature")
    ax[1,2].set_xlabel("Date")
    ax[1,2].set_ylabel("tavg(℃)")
    ax[1,2].grid(True)

    for a in ax.flatten():
        a.xaxis.set_major_locator(mdates.YearLocator(5))
        a.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
        a.tick_params(axis='x', labelrotation=0, labelsize=9)
    
    fig.subplots_adjust(hspace=0.5)
    

    return plt.show()

def season_graph(filename):
    df = pd.read_csv(filename, skipinitialspace = True)
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["tavg"] = pd.to_numeric(df["tavg"], errors="coerce")
    df = df.sort_values("date")
    winter_df = df[df["month"].isin([12, 1, 2])].sort_values("date")
    
    
    summer_df = df[df["month"].isin([6, 7, 8])]
    winter_df = df[df["month"].isin([12, 1, 2])]
    fig, ax = plt.subplots(2, 1, figsize=(12, 6))
    for a in ax:
        a.xaxis.set_major_locator(mdates.YearLocator(5))
        a.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
        a.tick_params(axis='x', labelrotation=0, labelsize=9)


    ax[0].plot(summer_df["date"], summer_df["tavg"], color = "red")
    ax[0].set_title("summer temperature")
    ax[0].set_xlabel("Date")
    ax[0].set_ylabel("tavg(℃)")
    ax[0].grid(True)
    

    ax[1].plot(winter_df["date"], winter_df["tavg"], color = "blue")
    ax[1].set_title("winter temperature")
    ax[1].set_xlabel("Date")
    ax[1].set_ylabel("tavg(℃)")
    ax[1].grid(True)
    
    fig.subplots_adjust(hspace=0.5)
    plt.tight_layout()

    return plt.show()

def my_birthday(filename):
    df = pd.read_csv(filename, skipinitialspace = True)
    df_bd = df[(df["month"] == 6) & (df["day"] == 5)]
    df_bd = df_bd.sort_values("year")

    years = df_bd["year"].astype(int)


    plt.figure(figsize=(10, 5))
    plt.plot(df_bd["year"], df_bd["tavg"])
    plt.title("June 5th Temperature")
    plt.xlabel("Year")
    plt.ylabel("tavg (℃)")
    plt.grid(True)

    plt.xticks(ticks=years, labels=years, rotation=90)

    plt.tight_layout()
    return plt.show()



def main():
    filename = "weather_146_1980_2024.csv"
    if not os.path.exists(filename):
        make_data()

    month_graph(filename)
    season_graph(filename)
    my_birthday(filename)
    


if __name__ == "__main__":
    main()