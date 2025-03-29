number = []

def main():
    while True:
        n = int(input("숫자를 입력하세요 (끝내려면 0 입력): "))
        
        if n == 0:
            break
        else:
            number.append(n)
    
    total = my_sum(number)
    print(f"총 합은 {total}입니다.")

def my_sum(num_list):
    total = 0
    for n in num_list:
        total += n
    return total

if __name__ == "__main__":
    main()