
import random

def lotto():
    lotto_nums = []
    while len(lotto_nums) < 6:
            num = random.randint(1, 45)
            if num not in lotto_nums:
                lotto_nums.append(num)
    return lotto_nums


def main():
    print(lotto())

if __name__ == "__main__":
    main()