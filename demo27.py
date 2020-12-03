def a(*person):  #可变参数,得到的是列表  若为两个**则为字典
    '''功能：计算bmi
        person:可变参数，分别为：姓名，身高，体重
    '''
    
    for b in person:     #b为带有3个参数的列表
        for c in b:      #c为获取每个元素
            d = c[0]
            e = c[1]
            f = c[2]
            print(d +"的身高："+str(e)+"米\t 体重："+str(f)+"千克")
            bmi = f/(e*e)
            print("你的bmi指数为："+str(bmi))
            if bmi<18.5:
                print("过轻")
            if bmi>=18.5 and bmi<24.9:
                print("正常范围")
            if bmi>=24.9 and bmi<29.9:
                print("过重")
    print(b)

g =(['录入',1.83,60],["路人",1.80,70])
a(g)
      
            
                   
