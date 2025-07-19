def delete_alpha(s):
    res=''
    for i in s:
        if i in 'abcdfghjklmnpqrstvwxyz':
            res=res+(i,'')
    return res
inp=input()
print(delete_alpha(inp))
