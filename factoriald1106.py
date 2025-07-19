##def factorial(n):
##    if n==0:
##        return 1
##    else:
##        return n*factorial(n-1)
##print('factorial of 3:',factorial(3))
##

def factorial(n):
    assert(n>=0),"factorial of negative no is not defined"
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n=int(input())
try:
    print('factorial of n:',factorial(n))
except AssertionError as ob:
    print(ob)
print("Thank you")


