


def my_sum(num):
    total = 0
    for n in range(1,num+1):
        total += n
    return total

def main():
    n = int(input("숫자를 입력하세요 : "))
        
    print(f"1부터 {n}까지의 합은 {my_sum(n)}입니다.")


if __name__ == "__main__":
    main()