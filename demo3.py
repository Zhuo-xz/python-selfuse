print("\n手机店打折活动进行中……")
week = input("请输入中文星期（如星期一）")  #请输入中文星期
time = int(input("请输入小时，如（0~23）")) #请输入时间
if (week == "星期二" and (time >= 10 and time <= 11)) or (week == "星期五" and (time >= 14 and time <= 15)):
    print("恭喜您")
if not (week == "星期二" and (time >= 10 and time <= 11)) or (week == "星期五" and (time >= 14 and time <= 15)):
    print("很遗憾")
 

