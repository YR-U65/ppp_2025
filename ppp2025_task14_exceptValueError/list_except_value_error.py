

def whatnumber():
    numbers_list = []
    while True:
        numbers = input("숫자를 입력하세요. : ")
        try:
            nums = int(numbers)
            if nums != -1 and type(nums) == int and nums > 0 :
                numbers_list.append(nums)
            elif nums == -1 :
                return numbers_list
            else:
                nums = None
        except ValueError:
            nums = None


def main():
    nums = whatnumber()
    print(f"입력된 값은 {nums} 입니다. 총 {len(nums)}개의 자연수가 입력되었고, 평균은 {sum(nums)/len(nums)}입니다.")


if __name__ == "__main__" :
    main()