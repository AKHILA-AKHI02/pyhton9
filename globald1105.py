x=5;y=7
def changeme(mylist_var):
    p=89
    global x,y
    x=y+2
    mylist=[1,2,3,4]
    print("Values inside the function:",mylist)
    print("Local variables the function:",locals())
    print("global variables are:",globals())
    return
mylist_var=[10,20,30]
changeme(mylist_var)
print("values outside the function:",mylist_var)
