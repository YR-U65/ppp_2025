



def read_db(filename):
    calorie_db = {}
    with open(filename, encoding = "utf-8-sig") as f:
        lines = f.readlines()
        for line in lines[1:]:
            line = line.strip()
            tokens = line.split(",")
            calorie_db[tokens[0]] = int(tokens[1])/int(tokens[2])
    return calorie_db



def what_fruit(name):
    fruit_list = []

    while True:
        name = input("어떤 것을 드셨습니까?(종료 = 0):")
        if name == '0':
            break
        fruit_list.append(name)

    return fruit_list



def fruit_g(name_dic):
    fruit_eat={}

    for name in name_dic:
        fruit_eat[name] = int(input(f"{name}을(를) 몇 g 드셨습니까?: "))

    return fruit_eat
        
    

def fruit_calculator(fruit_dic, fruit_calorie_db):
    total = 0
    for name in fruit_dic:
        total += fruit_dic[name] * fruit_calorie_db[name]

    return total





def main():
    fruit_calorie_db = read_db("ppp2025_4/week_6/calorie_db.csv")
    fruit_name = what_fruit(None)
    how_much = fruit_g(fruit_name)


    print(f"드신 것은 {fruit_name}이며 총 칼로리는 {fruit_calculator(how_much, fruit_calorie_db):.0f}kcal입니다.")



if __name__ == "__main__" :
    main()