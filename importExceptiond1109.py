try:
    import abc1
except ImportError as ob:
    print(ob)
try:
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
    res=num1/num2
except Exception as ob:
    print(ob)
else:
    print(num1,'/',num2,'=',res)
