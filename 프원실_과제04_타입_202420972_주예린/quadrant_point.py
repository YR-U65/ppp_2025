
x= int(input("x의 좌표: "))
y = int(input("y의 좌표: "))


#if문으로 범위 나눠주기
if 0 < x and 0 < y :
    print(f"점 ({x}, {y})는 1사분면 입니다. ")

elif x < 0 and 0 < y :
    print(f"점 ({x}, {y})는 2사분면 입니다. ")

elif x < 0 and y < 0 :
    print(f"점 ({x}, {y})는 3사분면 입니다. ")

elif 0 < x and y < 0 :
    print(f"점 ({x}, {y})는 4사분면 입니다. ")

elif x == 0 and y == 0 :
     print(f"점 ({x}, {y})는 원점 입니다. ")

elif x == 0 : 
     print(f"점 ({x}, {y})는 y축 위에 있습니다. ")

elif y == 0 :
     print(f"점 ({x}, {y})는 x축 위에 있습니다. ")

