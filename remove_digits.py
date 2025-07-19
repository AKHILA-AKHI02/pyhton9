##def remove_digits(s):
##    temp=''
##    d='0123456789'
##    for i in s:
##        if i not in d:
##            temp=temp+i
##    return temp
##inp=input()
##print(remove_digits(inp))


def remove_digits(s):
    d='0123456789'
    for i in d:
        s=s.replace(i,'')
    return s
inp=input()
print(remove_digits(inp))

###O/p:1:
##today is 7th day of 3rd month of year 2024
##today is th day of rd month of year
###O/P:2:
##my mobile number begins with 99 and ends with 71
##my mobile number begins with  and ends with 
##
