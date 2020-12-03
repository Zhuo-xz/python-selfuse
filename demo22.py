##正则表达式：定义一个规则，检查是否匹配
import re
a = r'mr_\w'
b = 'MR_SHOP mr_shop'
c = re.match(a,b,re.I)
print(c)
print(c.start())
print(c.end())
print(c.group())  #若结果不存在则会出现错误
print("")


import re
d = r'(13[4-9]\d{8})|(15[01289]\d{8})$'
e = "13634222222"
f = re.match(d,e)    #若无则为None  re.i 不区分字母大小写
g = re.search(d,e)   #若无则为None  re.A  让\w不匹配汉字
h = re.findall(d,e)
print(f)
print(g)
print(h)
