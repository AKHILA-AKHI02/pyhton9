from collections import Counr
def counter(s:str,n:int)->list:
    
    s=s.lower()
    s=s.replace(" ","")
    n=Counter(s)
    res=n.most_common(n1)
    rs=[i[0] for i in res]
    return ''.join(rs)
inp=input()
n1=int(input())
print(counter(inp,n1))



#o/p:
#educate
#4
#educ
