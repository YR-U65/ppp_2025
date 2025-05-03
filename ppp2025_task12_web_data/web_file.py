import os
import requests


def download_data(place, year, filename):
    URL = f"https://api.taegon.kr/stations/{place}/?sy={year}&ey={year}&format=csv"
    with open(filename, "w", encoding="UTF-8-sig") as f:
        req = requests.get(URL)
        req.encoding = "UTF-8"
        f.write(req.text)


def data_column(filename, column):
    weather_data = []
    with open(filename, encoding="UTF-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:] :
            tokens = line.split(",")
            weather_data.append(float(tokens[column]))
    return weather_data


def avg_calculate(data):
    return f"{sum(data)/len(data):.1f}"


def rainfall_days_calculate(data, n):
    days = 0
    for datas in data:
        if datas >= n:
            days += 1
    return days


def make_file(newfile, title, data):
    with open(newfile, encoding="UTF-8-sig") as f:
        lines = f.readlines()
        if not lines:
            with open(newfile, "w", encoding="UTF-8-sig") as f:
                f.write(title + "\n" + str(data))
                
        else:    
            new_title = lines[0].strip("\n") + f", {title}"
            new_data = lines[1].strip("\n") + f", {data}"
        
            with open(newfile, "w", encoding="UTF-8-sig") as f:
                f.write(new_title + "\n")
                f.write(str(new_data) + "\n")


def main():
    filename = "./weather(146)_2020-2020.csv"
    if not os.path.exists(filename):
        download_data(146, 2020, filename)

    tavg_year = avg_calculate(data_column(filename, 4))
    n = 5
    rainfall = data_column(filename, 9)
    rainfall_days = rainfall_days_calculate(rainfall, n)
    total_rainfalls = sum(rainfall)

    newfilename = "./HW_12_file_input.csv"
    if not os.path.exists(newfilename):
        with open(newfilename, "w", encoding="UTF-8-sig") as f:
            f.write("")
            
    make_file(newfilename, "tavg_y", tavg_year)
    make_file(newfilename, f"rfdays(>={n}mm)", rainfall_days)
    make_file(newfilename, "total_rf", total_rainfalls)


if __name__ == "__main__":
    main()