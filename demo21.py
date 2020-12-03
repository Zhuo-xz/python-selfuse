import math  #导入数学模块
print("以货币的形式显示${:,.2f}".format(1251+3950))
print("{0:.1f}用科学计数法表示:{0:E}".format(120000.1)) #  E表示科学计数法
print("Π取5位小数:{:.5f}".format(math.pi))
print("{0:d}的十六进制是:{0:#x}".format(100))   # #x表示十六进制
print("天才是有{:.0%}的灵感,加上{:.0%}的汗水。".format(0.01,0.99))
