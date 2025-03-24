


tc=int(input("화씨(℃) 온도를 입력하세요. : "))


def tf(a): #섭씨를 화씨로 변환하는 함수
    tempf = a*9/5+30
    return tempf


print(f"{tc}℃는 {tf(tc)}℉ 입니다.")
