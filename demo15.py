a = ("python",28,('abc','qwe'),['u','i','o'])
b = a[2:4]
print(b)

##元组推导式
import random
c = (random.randint(10,100) for i in range(10))
print(c)
print(tuple(c))
d = (random.randint(10,100) for i in range(10))
print(d.__next__() )  #输出第一个元素
print(d.__next__() )  #输出第二个元素
print(d.__next__() )  #输出第三个元素

##对生成器对象访问后，对象就不存在了

