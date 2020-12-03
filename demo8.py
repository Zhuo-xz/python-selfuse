a = "希望之酒，失望之杯","??"
print(a[1])  # 1输入元素2
print(a[0])  # 0输入元素1
print(a[-1]) # -1输入倒数元素1
##切片教学    sname[start:end:step]
b = "元素1","元素2","元素3","元素4","元素5","元素6","元素7","元素8"
print(b[1:5])
print(b[1:5:2])
c = a + b
print(c)
##只能是同类型的序列相加
##列表+列表 元组+元组 字符串+字符串
d = enumerate(b)
print(d)
