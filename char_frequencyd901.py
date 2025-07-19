##def char_frequency(s):
##    d=dict()
##    for i in s:
##        if i.isalpha():
##            d[i]=s.count(i)
##    return d
##inp=input()
##print(char_frequency(inp))


#o/p:
#hello world
#{'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}



def char_frequency(s): #2
    d=dict()
    for i in s:
        if i.isalpha():
            if i not in d:
                d[i]=s.count(i)
    return d
inp=input()
print(char_frequency(inp))
