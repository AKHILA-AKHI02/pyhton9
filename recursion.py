def factorial(a,b):
    assert(b!=0),"divisble by zero not "
    return a/b

a=int(input())
b=int(input())
try:
    print(factorial(a,b))
except AssertionError as ob:
    print(ob)

