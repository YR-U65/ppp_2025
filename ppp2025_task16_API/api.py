from sfarm_hw import submit_to_api

import os
import requests


def download_data(place, year, filename):
    URL = f"https://api.taegon.kr/stations/{place}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        req = requests.get(URL)
        req.encoding = "UTF-8"
        f.write(req.text)

def weather_date(name):
    weather_data = []

    with open(name, encoding=("utf-8-sig")) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_data.append([int(tokens[0]), int(tokens[1]), int(tokens[2])])

    return weather_data

def data_column(filename, column):
    weather_data = []
    with open(filename, encoding="UTF-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:] :
            tokens = line.split(",")
            weather_data.append(float(tokens[column]))
    return weather_data

def weather_diff(date, tmax, tmin):
    
    max_gap = tmax[0] - tmin[0]
    max_gap_date = date[0]

    for i in range(1, len(date)):
        diff = tmax[i] - tmin[i]
        if max_gap < diff :
            max_gap = diff
            max_gap_date = date[i]

    return max_gap, max_gap_date

def filename(year, place = 146):
    filename = f"weather({place})_{year}.csv"
    if not os.path.exists(filename):
        download_data(place, year, filename)
    return filename


def main():
    filename2015 = filename(2015)
    filename2022 = filename(2022)
    filename2024 = filename(2024)
    filename2024_suwon = filename(2024, 119)
    filename2024_date = weather_date(filename2024)
    filename2024_tmax = data_column(filename2024, 3)
    filename2024_tmin = data_column(filename2024, 5)
    total_rainfall_2024_146 = sum(data_column(filename2024, 9))
    total_rainfall_2024_119 = sum(data_column(filename2024_suwon, 9))
    
    total_rainfall_2015_146 = round(sum(data_column(filename2015, 9)), 1)
    max_tavg_2022_146 = round(max(data_column(filename2022, 4)), 1)
    max_diff_2024, diff_date_2024 = weather_diff(filename2024_date, filename2024_tmax, filename2024_tmin)
    diff_119_146 = round(abs(total_rainfall_2024_119 - total_rainfall_2024_146), 1)


    name = "주예린"
    affiliation = "스마트팜학과"
    student_id = "202420972"

    answer1 = total_rainfall_2015_146
    answer2 = max_tavg_2022_146
    answer3 = max_diff_2024
    answer4 = diff_119_146

    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)



if __name__ == "__main__":
    main()