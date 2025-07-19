def demo_yield():
    print("code segement1 executed")
    x=7
    yield x*x
    print("code segement2 executed")
    yield x+x
    print("code segement3 exxecuted")
    yield x-x
    print("code segement4 executed")

#o/p:
    x=demo_yield()
type(x)
<class 'generator'>
next(x)
code segement1 executed
49
next(x)
code segement2 executed
14
next(x)
code segement3 exxecuted
0
next(x)
code segement4 executed
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    next(x)
StopIteration

