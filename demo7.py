b = (99)
for a in range(1,100):
    if a % 7 == 0:
        continue
    else:
        c = str(a)
        if c.endswith("7"):
            continue
        else:
            b -= 1
print("从1数到99共拍桌子：",b)
