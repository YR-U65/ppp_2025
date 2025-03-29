def main() :
    total_calory()

fruits_ate_calories = []

calories = {'한라봉' : 50, '딸기' : 34, '바나나' : 77}

def total_calory():

    while True : 
        fruit_ate = input("한라봉, 딸기, 바나나 중에 어떤 과일을 드셨나요? (칼로리 계산 : 0) : ")

   
        if fruit_ate != '0' : 
            how_much_ate = int(input("얼마나 드셨나요?(g) : "))
            calories_calculation = (calories[fruit_ate]/100) * how_much_ate

            fruits_ate_calories.append(calories_calculation)

        elif fruit_ate == '0' :
            total_calories = sum(fruits_ate_calories)
            print(f"먹은 과일의 총 칼로리는 {total_calories}입니다.")

            break


if __name__ == "__main__" :
    main()

