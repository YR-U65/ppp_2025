
how_much_star = int(input("몇 줄의 삼각형을 그리시겠습니까? :"))

for i in range(how_much_star+1) :
    print(f"{('*' * (2*i-1)):^30}")