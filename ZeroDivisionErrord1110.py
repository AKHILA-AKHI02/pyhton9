try:
    num1=int(input())
    num2=int(input())
except ValueError as ob:
    print(ob)
else:
    try:
        res=num1/num2
    except ZeroDivisionError as oob:
        print(ob)
    else:
        print(res)
