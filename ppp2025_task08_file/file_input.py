



def read_str(str):
    txt = ""
    with open(str) as f:
        lines = f.readlines()
        for line in lines:
            txt += " " + line.strip()
    return txt
            



def str2num(str):
    str_list = str.split()
    nums = [int(n) for n in str_list]
    return nums


def average(n):
    return sum(n)/len(n)

def median(n):
    n_sorted = sorted(n)
    return n_sorted[len(n)//2]




def main():
    numbers = read_str("ppp2025_task08_file/task_numbers.txt")
    nums = str2num(numbers)
    print(f"주어진 숫자는 {nums}")
    print(f"총 숫자의 갯수는 {len(nums)}")
    print(f"주어진 숫자의 평균은 {average(nums)}")
    print(f"숫자들의 최댓값은 {max(nums)}")
    print(f"숫자들의 최솟값은 {min(nums)}")
    print(f"숫자들의 중앙값은 {median(nums)}")





if __name__ == "__main__":
    main()