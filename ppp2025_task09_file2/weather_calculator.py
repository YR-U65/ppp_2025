


def read_weather_db(filename):
    weather_db = []

    with open(filename, encoding = "utf-8-sig") as f:
        lines = f.readlines()
        inventory_raw = lines[0].strip()
        inventory_new = inventory_raw.split(",")
        inventory_new = inventory_new[3:]

        inventory = []
        for i in inventory_new :
            inventory.append(i.strip())


        for line in lines[1:]:
            line = line.strip()
            part = line.split(",")
            date = f"{part[0]}-{part[1]}-{part[2]}"
            value = part[3:]
            data_list = {"date" : date}

            for i in range(len(inventory)):
                data_list[inventory[i]] = float(value[i])
            weather_db.append(data_list)

    return weather_db

            

            
def average_tp(db):
    tavg_list = []
    for tavg in db :
        if "tavg" in tavg:
            tavg_list.append(tavg["tavg"])

    return sum(tavg_list)/len(tavg_list)        




def rainy_days(n, db):
    rainydays_list = []
    for rainy in db :
        if "rainfall" in rainy:
            rainydays_list.append(rainy["rainfall"])
    
    rainydays = []
    for i in range(len(rainydays_list)):
        days = rainydays_list[i]
        if days >= n :
            rainydays.append(days)
    return len(rainydays)




def total_rainyfall(db):
    rainydays_list = []
    for rainy in db :
        if "rainfall" in rainy:
            rainydays_list.append(rainy["rainfall"])
    return sum(rainydays_list)




def main():
    n = 5
    year = 2022
    weather_db = read_weather_db("ppp2025_task09_file2/weather(146)_2022-2022.csv")

    print(f"{year}년 연 평균 기온은 {average_tp(weather_db):.1f}℃, {n}mm 이상 강우 일수는 {rainy_days(n, weather_db)}일, 총 강우량은 {total_rainyfall(weather_db):.1f}mm 입니다.")



if __name__ == "__main__":
    main()