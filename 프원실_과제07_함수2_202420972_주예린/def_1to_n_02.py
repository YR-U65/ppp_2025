

def get_range_list(n):
    numbers=[]
    for i in range(1,n+1) :
        numbers.append(i)
    return numbers



def main():
    what_number = int(input("n => "))
    

    print(f"현재 숫자 리스트는 {get_range_list(what_number)}입니다.")



if __name__ == "__main__":
    main()