##格式化
a = "编号：%09i\t公司名称：%s \t 官网：http://www.%s.com"  #定义模板
b = (7,"百度","baidu")
print(a%b)
c = "编号：{:0>9s}\t公司名称：{:s} \t 官网：http://www.{:s}.com"
d = c.format("7","百度","baidu")
print(d)

