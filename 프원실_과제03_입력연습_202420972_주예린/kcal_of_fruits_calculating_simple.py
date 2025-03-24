
#한라봉,딸기,바나나 각각 1g당 칼로리로 바꿔주기
hallabong = 50/100
strawberry = 34/100
banana = 77/100

#input으로 값 받기
fruit_ate = input("한라봉, 딸기, 바나나 중에 어떤 과일을 드셨나요?(명사) : ")
how_much_ate = int(input("얼마나 드셨나요?(g) : "))

#if문으로 세 가지 나눠주기
if fruit_ate == '한라봉' :
   calorie_calculation =  hallabong * how_much_ate

elif fruit_ate == '딸기' :
    calorie_calculation = strawberry * how_much_ate

else:
    calorie_calculation = banana * how_much_ate

print(f"{fruit_ate}을(를) {how_much_ate}g 만큼 섭취하셨습니다. 섭취하신 총 칼로리는 {calorie_calculation}kcal 입니다.")