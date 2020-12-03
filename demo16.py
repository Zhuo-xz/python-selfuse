##字典
a = {}
b = {'che':'车','chen':'臣','cheng':'称','chi':'吃'}
key = ('che','chen','cheng','chi')  #索引（键）必须为元组
value = ('车','臣','称','吃')   #正文汉字（值）可以是元组或列表
c = dict(zip(key,value))
d = {key:value}
print(a)
print(b)
print(c)
print(d)
e = dict.fromkeys(key)  #只有值的字典
print(e)

print(c.get("che"))
print(c.get("ch"))
print(c.get("ch","查无此音节"))
