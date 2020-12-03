def division():
    
    a = int(input("除数："))
    b = int(input("被除数："))
    
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
    except ZeroDivisionError as e: # 被除数为0的异常
        print(e)   
    except ValueError as f:   # 除数不为整数的异常
        print(f)
    except (ValueError,ZeroDivisionError) as g: # 将二者整合
        print(g)

    else:
        print("顺利整除")
    finally:
        print("一定执行的语句")
