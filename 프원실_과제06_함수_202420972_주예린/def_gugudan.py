def main() :
    gugudan()

n = int(input("몇 단? :"))


def gugudan():
    for i in range(1,10):
        gugudan_n = i * n
        print(f"{n} * {i} = {gugudan_n}")



if __name__ == "__main__" :
    main()
