a = "人生苦短，我用python"
print(len(a))   #计算字符
##计算字节
print(len(a.encode()))   #默认使用UTF—8解码（中文占3个字节）
print(len(a.encode("gbk")))  #  使用GBK解码（中文占2个字节）
