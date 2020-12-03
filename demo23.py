import re
a = r'1[34578]\d{9}'
b = "中奖号码：84978981 联系电话：13611111111"
c = re.sub(a,"1XXXXXXXXXXX",b)
print(c)
print("")


d = r'[?|&]'
e = "http://www.baidu.com"
f = re.split(d,e)
print(f)
