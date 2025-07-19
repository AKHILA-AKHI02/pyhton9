def test(s,n=2):
    s=str(s)
    s=s.split('.')
    res=''
    if len(s[1])>n:
        res=s[0]+'.'+s[1][:2]
    elif len(s[1])<n:
        res=s[0]+'.'+s[1]+'0'*(n-len(s[1]))
    else:
        res=s[0]+'.'+s[1]
    return res
inp=float(input())
print(test(inp,2))


#o/p:
#12
#12.00
#12.3
#12.30
