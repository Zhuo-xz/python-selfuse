#元组用小括号，列表用中括号，但元组一般不可修改
a = ("大家好")  #字符串
print(a)
print(type(a))
b = ("大家好",)  #元组
print(b)
print(type(b))

c = tuple(range(2,21,2))
print(c)
d = list(range(2,21,2))
print(d)
