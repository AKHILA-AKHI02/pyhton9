def frequent(s):
    s=s.upper()
    s=s.replace(' ','')
    a={}
    for i in s:
        if i in a:
            a[i]=a[i]+1
        else:
            a[i]=1
    return a
inp=input()
print(frequent(inp))
            
#o/p:
#hello world
#{'H': 1, 'E': 1, 'L': 3, 'O': 2, 'W': 1, 'R': 1, 'D': 1}
