print("今有不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何\n")
a = True
b = int(23)
while a:
    b += 1
    if b%3 == 2 and b%5 == 3 and b%7 == 2:
        print("答案为：",b)
        a = False
