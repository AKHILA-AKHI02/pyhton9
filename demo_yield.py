def demo_yield():
    a='python'
    print("code segement1 executed:",a)
    yield len(a)
    b='java'
    print("code segement2 executed:",b)
    yield len(b)
    c='visualC++'
    print("code segement3 executed:",c)
    yield len(c)
    d="VB"
    print("code segement4 executed:",d)
    yield len(d)
x=demo_yield()
print(next(x))
print(next(x))
print(next(x))
print(next(x))



#o/p:1
code segement1 executed: python
6
code segement2 executed: java
4
code segement3 executed: visualC++
9
code segement4 executed: VB
2

#o/p:2
x=demo_yield()
print(next(x))
code segement1 executed: python
6
print(next(x))
code segement2 executed: java
4
print(next(x))
code segement3 executed: visualC++
9
print(next(x))
code segement4 executed: VB
2






