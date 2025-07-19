def sum_series(a,b):
    assert (a<b),"first argument should be smaller than second."
    total=0
    for i in range(a,b,1):
        total=total+i
        yield total
n=int(input())
n1=int(input())
ob=sum_series(n,n1)
#o/p:
10
20
next(ob)
10
next(ob)
21
next(ob)
33
next(ob)
46
next(ob)
60
next(ob)
75
next(ob)
91
next(ob)
108
next(ob)
126
next(ob)
145
next(ob)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    next(ob)
StopIteration
