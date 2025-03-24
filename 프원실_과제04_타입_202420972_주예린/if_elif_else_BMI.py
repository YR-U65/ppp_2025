import math

weight = int(input("몸무게를 입력하세요(kg): "))
height = int(input("키를 입력하세요(cm): "))

#키를 cm로 받았으니 m로 변환해주기기
height_m = height/100

BMI = weight / height_m**2

'''“2020년 비만 진료지침에서는 체질량지수(BMI) △23~24.9kg/㎡를 비만 전단계 
△25~29.9kg/㎡를 1단계 비만 △30~34.9kg/㎡를 2단계 비만 △35kg/㎡이상을 3단
계 비만으로 정의했다'''

#if문으로 범위 나눠주기
if BMI<=18.5 :
    print(f"당신의 BMI 지수는 {BMI : .1f}kg/㎡ 이며 저체중 입니다.")

elif 18.5 <= BMI < 23 : 
    print(f"당신의 BMI 지수는 {BMI : .1f}kg/㎡ 이며 정상 입니다.")

elif 23 <= BMI < 25 : 
    print(f"당신의 BMI 지수는 {BMI : .1f}kg/㎡ 이며 비만 전단계 입니다.")

elif 25 <= BMI < 30 :
    print(f"당신의 BMI 지수는 {BMI : .1f}kg/㎡ 이며 1단계 비만 입니다.")

elif 30 <= BMI < 35 :
    print(f"당신의 BMI 지수는 {BMI : .1f}kg/㎡ 이며 2단계 비만 입니다.")

else :
    print(f"당신의 BMI 지수는 {BMI : .1f}kg/㎡ 이며 3단계 비만 입니다.")

#자바나 C에서는 elif 25 <= BMI and BMI < 30 이렇게 써야함
#숫자 중간에 BMI 넣는 건 파이썬에서만 가능함