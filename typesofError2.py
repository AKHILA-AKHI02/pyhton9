n=input("Enter a number:")
n1=input("Enter a number:")
try:
    import cde
    res=int(n)/int(n1)
except(ZeroDivisionError,ValueError,TypeError):
    print("Division by zero not allowed or string are not allowed.")
except Exception as ob:
    print(ob)
else:
    print(res)
print("vist again at module")
