def delete_vowels(s):
    d='AEIOUaeiou'
    for i in d:
        s=s.replace(i,'')
    return s
inp=input()
print(delete_vowels(inp))
