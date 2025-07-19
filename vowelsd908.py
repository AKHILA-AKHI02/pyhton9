def vowels(s):
    d='aeiouAEIOU'
    nd=0
    for i in s:
        if i in d:
            nd+=1
    return nd
def extractDigits(s):
    res=''
    d='0123456789'
    for i in s:
        if i in d:
            res+=i
    return res
def countdigit(s):
    d='0123456789'
    nd=0
    for i in s:
        if i in d:
            nd+=1
    return nd
def extractvowels(s):
    res=''
    d='aeiouAEIOU'
    for i in s:
        if i in d:
            res+=i
    return res
n=input()
print(vowels(n))
print(extractvowels(n))
print(countdigit(n))
print(extractDigits(n))



#o/p:
#today
2
oa
0

    
        
