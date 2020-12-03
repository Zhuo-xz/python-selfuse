a = "@小明 @小红 @小刚 @小亮"
b = a.split(" ")  #用空格分割字符串
print(b)
for i in b:
    print(i[1:]) #输出，并去掉@

c = ["小明","小红","小刚","小亮"]
d = '@' + " @".join(c)    #用空格和@连接
print(d)


print(a.count("@")) #出现次数

print(a.find("@"))  #首次出现位置  index同find 但是没有会发生错误
print(a.rfind("@"))  #最后出现位置
print(a.find("#"))  #没有显示—1

print(a.startswith("@"))
print(a.endswith("亮"))


