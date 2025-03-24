
import math

weight = int(input("몸무게를 입력하세요(kg): "))
height = int(input("키를 입력하세요(cm): "))

#키를 cm로 받았으니 m로 변환
height_m = height/100

#math 넣었으니 **2 보다는 pow 사용용
BMI = weight / math.pow(height_m,2)

print(f"당신의 BMI 지수는 {BMI}입니다.")