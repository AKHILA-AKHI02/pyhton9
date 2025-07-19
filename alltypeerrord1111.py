n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
try:
    res1=n1+n2
    res=int(n1)/int(n2)
except ZeroDivisionError:
    print("Division by zero not allowed")
except ValueError:
    print("String are not allowed.please input only integers")
except TypeError:
    print("Division on string not allowed")
except Exception as ob:
    print(ob)
else:
    print(res)
    print(res1)
finally:
    print("Thanks")
