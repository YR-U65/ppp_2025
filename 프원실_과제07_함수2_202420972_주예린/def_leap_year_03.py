


def is_leap_year(y) :
    if (y % 4 == 0 and y % 100 != 0) or y % 400 ==0:
        return "윤년입니다."
    else:
        return "윤년이 아닙니다."



def main():
    year = int(input("몇 년도입니까?: "))

    print(f"{year}년도는 {is_leap_year(year)}")

if __name__ == "__main__" :
    main()