

def weather(name, n=[]):
    weather_data = []

    for i in range(len(n)):
        weather_data.append([])

    with open(name, encoding=("utf-8-sig")) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            for i in range(len(n)):
                if int(tokens[0]) == n[i]:
                    weather_data[i].append([int(tokens[0]), int(tokens[1]), int(tokens[2])])

    return weather_data



def weather_datas(name, n=[], col_ind = 0):
    weather_ind = []

    for i in range(len(n)):
        weather_ind.append([])

    with open(name, encoding=("utf-8-sig")) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            for i in range(len(n)):
                if int(tokens[0]) == n[i]:
                    weather_ind[i].append(round(float(tokens[col_ind]),1))
    return weather_ind



def years_f_t(from_n, to_n):
    y = []
    for i in range(from_n, to_n+1):
        y.append(i)
    return y



def weather_diff(date, tmax, tmin):
    
    diff_max = []
    diff_date = []
    for i in range(len(date)):
        max_gap_date = date[i][0]
        max_gap = tmax[i][0]-tmin[i][0]
        for j in range(len(date[i])):
            dif = tmax[i][j] - tmin[i][j]
            if max_gap < dif :
                max_gap = dif
                max_gap_date = date[i][j]
            
        diff_max.append(round(max_gap,1))
        diff_date.append(max_gap_date)
    return diff_max, diff_date



def arrange(diff_date, diff_gap) :
    result = ""
    for i in range(len(diff_date)):
        date = diff_date[i]
        gap = diff_gap[i]
        result += f"{date[0]}-{date[1]}-{date[2]} : {gap}℃\n"
    return result



def weather_months(name, n=[], month = []):
    weather_data = []

    for i in range(len(n)):
        weather_data.append([])

    with open(name, encoding=("utf-8-sig")) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            for i in range(len(n)):
                if int(tokens[0]) == n[i]:
                    for j in range(len(month)):
                        if int(tokens[1]) == month[j]:
                            weather_data[i].append([int(tokens[0]), int(tokens[1]), int(tokens[2])])

    return weather_data



def weather_months_datas(name, n=[], month = [], col_ind = 0):
    weather_ind = []

    for i in range(len(n)):
        weather_ind.append([])

    with open(name, encoding=("utf-8-sig")) as f:
        lines = f.readlines()
        for line in lines[1:]:
            tokens = line.split(",")
            for i in range(len(n)):
                if int(tokens[0]) == n[i]:
                    for j in range(len(month)):
                        if int(tokens[1]) == month[j]:
                            weather_ind[i].append(round(float(tokens[col_ind]),1))
    return weather_ind



def gdd_calculator(date, tavg, n):
    temp_gdd = []
    for i in range(len(date)):
        temp_gdd.append([])

    for i in range(len(date)):
        temp_cum = 0
        for j in tavg[i]:
            if j >= n :
                temp_cum += (j-n)
        temp_gdd[i].append(round(temp_cum,1))
    return temp_gdd



def gdd_arrange(gdd_date, gdd_tp) :
    result = ""
    for i in range(len(gdd_date)):
        date = gdd_date[i]
        gdd = gdd_tp[i]
        result += f"{date[0][0]} : {gdd}℃ \n"
    return result



def gdd_over(date, tavg, n, m):
    temp_gdd_over = []
    gdd_over_date = []
    for i in range(len(date)):
        temp_cum = 0
        for j in range(len(tavg[i])):
            temp = tavg[i][j]
            if temp >= n :
                temp_cum += (temp-n)
            if temp_cum >= m+0.01:
                gdd_date = date[i][j]
                break
        temp_gdd_over.append(round(temp_cum,1))
        gdd_over_date.append(gdd_date)
                
    return temp_gdd_over, gdd_over_date



def main():
    filename = "ppp2025_task11_deep_data/weather(146)_2001-2022.csv"
    years = years_f_t(2001, 2022)
    months = 5, 6, 7, 8, 9
    n = 5
    m = 200
    date = weather(filename, n = years)
    tmax = weather_datas(filename, n = years, col_ind = 3)
    tmin = weather_datas(filename, n = years, col_ind = 5)
    diff_gap, diff_date = weather_diff(date, tmax, tmin)
    tavg = weather_months_datas(filename, n = years, month = list(months), col_ind = 4)
    data_months = weather_months(filename, n = years, month = list(months))
    gdd = gdd_calculator(data_months, tavg, n)
    

    print(f"연간 최고 일교차 일수, 일교차는 \n {arrange(diff_date, diff_gap)} 입니다.\n")
    print(f"연간 GDD는 \n {gdd_arrange(data_months, gdd)} 입니다.")
    
    months_sp = 4, 5, 6, 7, 8, 9, 10, 11, 12
    tavg_gdd_over = weather_months_datas(filename, n = years, month = list(months_sp), col_ind = 4)
    data_months = weather_months(filename, n = years, month= list(months_sp))
    gdd_tp, gdd_date = gdd_over(data_months, tavg_gdd_over, n, m)

    print(f"연간 GDD가 {m}도를 넘는 최초 일은\n {arrange(gdd_date, gdd_tp)} 입니다.")
    
    
    
if __name__ == "__main__" :
    main()