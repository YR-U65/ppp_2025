def get_weather_data(fname, col_idx):
    weather_datas = []
    with open(fname, encoding=("utf-8-sig")) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(float(tokens[col_idx]))

    return weather_datas



def average(nums) :
    return sum(nums)/len(nums)


def rainfalls_days(nums, criteria):
    count = 0
    for num in nums:
        if num >= criteria:
            count += 1
    return count
#이 함수는 len([x for x in rainfalls if x >= 5]) 이 한줄이랑 똑같음

def get_rain_events(rainfalls):
    count = 0
    count_list = []
    for rain in rainfalls:
        if rain > 0:
            count += 1
        else :
            if count > 0:
                count_list.append(count)
                count = 0
    if count > 0 :
        count_list.append(count)
    return count_list

def get_rainfalls(rainfalls):
    count = 0
    
    count_list = []
    for rain in rainfalls:
        if rain > 0:
            count += rain
        else :
            if count > 0:
                count_list.append(count)
                count = 0
    if count > 0 :
        count_list.append(count)
    return count_list


def get_weather_data_int(fname, col_idx):
    weather_datas = []
    with open(fname, encoding=("utf-8-sig")) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            weather_datas.append(int(tokens[col_idx]))

    return weather_datas

def sumifs(rainfalls, months, selected = [6, 7, 8]) :
    total = 0
    for i in range(len(rainfalls)):
        rain = rainfalls[i]
        month = months[i]
        if month in selected:
            total += rain
    return total




def main() :
    filename = "C:/code/2025_ppp_python/ppp2025_task10_file3/weather(146)_2001-2022.csv"
    #1. 일평균 기온의 연평균
    tavgs = get_weather_data(filename, 4)
    print(f"연평균 기온(avg. of 일평균) = {average(tavgs) : .1f}℃")
    #2. 5mm 이상인 강우일수
    rainfalls = get_weather_data(filename, 9)
    print(f"5mm 이상 강우일수는 {rainfalls_days(rainfalls, 5)}일")
    #len([x for x in rainfalls if x >= 5])
    #3. 총 강우량
    print(f"총 강수량은 = {sum(rainfalls):,.1f}mm")
    #4. 최장 연속 강우일수
    print(f"최장 연속 강우일수는 {max(get_rain_events(rainfalls))}일")
    # 강우 이벤트 중 최고 강수량
    print(f"최고 강우량은 {max(get_rainfalls(rainfalls)):.1f}mm")
    #6. top3 of tmax
    top3_tmax = sorted(get_weather_data(filename,3))[-3:] #[::-1] ==처음부터 끝까지 거꾸로
    print(f"가장 높은 기온 3개는 {top3_tmax}")
    #
    months = get_weather_data_int(filename, 1)
    print(f"여름철 강수량은 {sumifs(rainfalls, months, selected = [6, 7, 8]):.1f}mm 입니다.")

    #8. 2021년, 2022년 총 강수량
    filename_20yr = "C:/code/2025_ppp_python/ppp2025_task10_file3/weather(146)_2001-2022.csv"
    years = get_weather_data_int(filename_20yr, 0)
    rainfalls = get_weather_data(filename_20yr, 9)
    print(f"2021년 총 강수량은 {sumifs(rainfalls, years, selected=[2021]):.1f}mm 입니다.")
    print(f"2022년 총 강수량은 {sumifs(rainfalls, years, selected=[2022]):.1f}mm 입니다.")


if __name__ == "__main__":
    main()