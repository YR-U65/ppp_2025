
import math

x1 = int(input("x1의 좌표: "))
y1 = int(input("y1의 좌표: "))
x2 = int(input("x2의 좌표: "))
y2 = int(input("y2의 좌표: "))

#점 거리
distance = math.sqrt((x2-x1)**2+(y2-y1)**2)

print(f"점 ({x1},{y1}) 와(과) 점 ({x2},{y2}) 사이의 거리는 {distance : .2f} 입니다.")