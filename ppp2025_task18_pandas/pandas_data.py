from sfarm_hw import submit_to_api

import requests
import pandas as pd

def download_data(place, year, filename):
    URL = f"https://api.taegon.kr/stations/{place}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        req = requests.get(URL)
        req.encoding = "UTF-8"
        f.write(req.text)

def main():
    files = {}
    dfs = {}
    for year in [2012, 2019, 2020, 2024]:
        files[year] = f"weather_146_{year}.csv"
        download_data(146, year, files[year])
        dfs[year] = pd.read_csv(files[year], skipinitialspace = True)

    filename = "weather_119_2019.csv"
    download_data(119, 2019, filename)
    dfs_119_2019 = pd.read_csv(filename, skipinitialspace = True)

    dfs[2020]["tdiff"] = dfs[2020]["tmax"] - dfs[2020]["tmin"]


    name = "주예린"
    affiliation = "스마트팜학과"
    student_id = "202420972"

    answer1 = round(dfs[2012]["rainfall"].sum(), 2)
    answer2 = round(dfs[2024]["tmax"].max(), 2)
    answer3 = round(dfs[2020]["tdiff"].max(), 2)
    answer4 = round(abs(dfs_119_2019["rainfall"].sum() - dfs[2019]["rainfall"].sum()), 2)

    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)

if __name__ == "__main__":
    main()