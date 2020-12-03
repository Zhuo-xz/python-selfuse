a = ["cat","Tom","Angela","pet"]
a.sort()        #区分字母大小写进行升序排列
print(a)
a.sort(key=str.lower)  #不区分字母大小写进行升序排列
print(a)
a.sort(key=str.lower,reverse=True)  #默认为Flase
print(a)   ##改变原序

b = sorted(a,key=str.lower,reverse=True)  #建立副本，不改变原序
print(b)
