

def average(nums) :
    return sum(nums) / len(nums)

def main():
    total = []
    while True :
        number = input("평균을 구하고 싶은 숫자를 입력하시오. : ")
        if number == '0' :
            break
    
        onetoone = [float(x) for x in number.split(",")]
        total.extend(onetoone)
        '''
        append == 덩어리 째로 추가시킴 만약 어떤 리스트에 입력한 숫자가 [5, 6] 이면 다른 리스트에 .append 썼을 때 [1, 2, [5, 6]] 이런 식으로 추가됨
        
        하지만 extend는 확장이라는 뜻에 가깝게 하나씩 꺼내서 추가시킴. 만약 리스트 숫자가 [5, 6] 이면 다른 리스트에 extend 사용시 [1, 2, 5, 6] 으로 추가됨
        '''

    print(f"입력하신 모든 숫자는 {total}입니다.")
    print(f"입력한 숫자의 평균은 {average(total) : .2f}입니다.")



if __name__ == "__main__" :
    main()