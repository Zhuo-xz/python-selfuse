a = [1,2,3,4,5,6,7,8]
print(a)
b = [10,11]
print(b)
a.append(9)  #添加元素  默认最后一位
print(a)
a.insert(0,0)  #第二位为位置
print(a)
a.extend(b)  #添加列表
print(a)
print("\n")


c = [1,2,2]
print(c)
c[2] = 3   #直接修改
print(c)
del c[2]
print(c)
print("\n")

d = "一行白鹭上青天"
e = list(d)
print(e)
e.remove("天")  #移除某个元素
print(e)
