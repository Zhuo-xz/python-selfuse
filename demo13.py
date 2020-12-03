import random  ##导入生成随机数的模块
a = []   #定义一个空列表
for i in range(10):
    a.append(random.randint(10,100))   #往空列表加入随机数
print(a)

###简化版
b = [random.randint(10,100) for i in range(10)]
print(b)
