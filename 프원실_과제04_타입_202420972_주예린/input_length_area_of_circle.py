import math

r = int(input("원의 반지름을 입력하세요(cm): "))
p = math.pi
area = p*(r**2) #원 면적
length = 2*p*r #원 둘레

#{어쩌구 : .소수점남길자리f} >>> 소수점 쉽게 남기는 법 round보다 편함
print(f"반지름이 {r}인 원의 둘레는 {length : .1f}cm 이고 면적은 {area : .2f}㎠ 입니다.")