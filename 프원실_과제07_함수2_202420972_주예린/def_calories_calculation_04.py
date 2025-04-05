


def total_calorie(fruits, fruits_calorie_dic) :
    total = 0
    for name in fruits:
        total += fruits[name]/100*fruits_calorie_dic[name]

    return total



def main():
    fruits_calorie_dic = {'한라봉' : 50, '딸기' : 34, '바나나' : 77}
    fruits = {"한라봉" : 150, "딸기" : 300}

    print(f"총 칼로리는 {total_calorie(fruits, fruits_calorie_dic):.0f}kcal 입니다.")





if __name__ == "__main__" :
    main()