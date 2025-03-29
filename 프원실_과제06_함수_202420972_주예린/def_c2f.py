def main() :
      tf()

tc=int(input("화씨(℃) 온도를 입력하세요. : "))


def tf(a):
    tempf = a*9/5+30
    return tempf


print(f"{tc}℃는 {tf(tc)}℉ 입니다.")

if __name__ == "__main__" :
    main()