##def add(arg1,arg2):
##    total=arg1+arg2
##    print("Inside the function:",total)
##    return total
##total=add(10,20)
##print("Outside the function:",total)


##total=100
##def add(arg1,arg2):
##    total=arg1+arg2;
##    print("Inside the function:",total)
##    return total
##a=add(10,20)
##print("Outside the function gobal variable:",total)


res=lambda arg1,arg2:arg1+arg2
print("value of total:",res(10,20))
print("value of total:",res(20,20))


#O/P:
#value of total: 30
#value of total: 40
