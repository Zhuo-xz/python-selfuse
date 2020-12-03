def division():    # 定义一个函数,括号内为形式参数
    a = int(input("除数："))
    b = int(input("被除数："))
    assert a>b,"除数小于被除数"  # 断言调试,仅仅用于调试
    c = a//b
    d = a-c*b
    print(c)
    if d >0:
        print("余数为",d)
    else:
        print("")
if __name__ == "__main__":
    try:
        division()
    except AssertionError as e:
        print(e)


def a():          # 定义一个空函数
    pass
