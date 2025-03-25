import math


print(f"{"각":<6} {"라디안" :<7} {"cos" :<10} {"sin" :<10} tan")


for i in range(361):
    trig_radian = math.radians(i)
    if math.tan(trig_radian) > 10 ** 10 :
        print(f"{i}˚{' ':<5} {trig_radian:<8.4f} {math.cos(trig_radian):<10.4f} {math.sin(trig_radian):<10.4f} infinity")

    else:
        print(f"{i}˚{' ':<5} {trig_radian:<8.4f} {math.cos(trig_radian):<10.4f} {math.sin(trig_radian):<10.4f} {math.tan(trig_radian):.4f}")