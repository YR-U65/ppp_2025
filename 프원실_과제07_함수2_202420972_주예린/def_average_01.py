


def average(nums) :
    return sum(nums) / len(nums)



def main():
    nums = []
    while True:
        numbers = float(input("숫자를 입력하세요(종료:0): "))
        if numbers == 0:
            break
        nums.append(numbers)
    
    print(f"평균은 {average(nums)} 입니다.")




if __name__ == "__main__" :
    main()