#나중에 계산할 리스트 미리 만들어주기
fruits_ate_calories = []

#각 과일 별로 딕셔너리 만들어서 값 변환 준비
calories = {'한라봉' : 50, '딸기' : 34, '바나나' : 77}


#칼로리 계산해달라고 할 때까지 값 받아서 리스트에 넣어 나중에 한꺼번에 계산하기
while True : #무한반복문
    fruit_ate = input("한라봉, 딸기, 바나나 중에 어떤 과일을 드셨나요? (칼로리 계산 : 0) : ")

    #if문으로 어디서 멈출지 결정하기
    if fruit_ate != '0' : 
        how_much_ate = int(input("얼마나 드셨나요?(g) : "))

        # 딕셔너리에 넣었던 값 바로 변환해서 먹은 만큼 계산하기
        calories_calculation = (calories[fruit_ate]/100) * how_much_ate

        #계산한 값은 바로 미리 만들어두었던 리스트에 넣어두기, 나중에 합산하려고.
        fruits_ate_calories.append(calories_calculation)

    #if문으로 사용자가 0 입력했을 때 멈추고 총 칼로리 계산하도록 설계
    elif fruit_ate == '0' :

        #그동안 리스트에 담아뒀던 값 한 번에 합산
        total_calories = sum(fruits_ate_calories)
        print(f"먹은 과일의 총 칼로리는 {total_calories}입니다.")

        break #무한반복문 중단