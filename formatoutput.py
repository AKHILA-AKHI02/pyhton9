print('{:#<30}'.format('Apple'))
print('{:*>30}'.format('Apple'))
print('{:^30}'.format('mouni'))
print("int:{0:d};hex:{0:x};oct:{0:o};bin{0:b}".format(42,55))
print("int:{1:d};hex:{1:x};oct:{1:o};bin{1:b}".format(42,55))
print('{:,}'.format(1234567890))
points=19.0;total=22
print('correct answers:{:.2%}'.format(points/total))
print('correct answers:{:.2}'.format(points/total))

#O/P:
Apple#########################
*************************Apple
            mouni             
int:42;hex:2a;oct:52;bin101010
int:55;hex:37;oct:67;bin110111
1,234,567,890
correct answers:86.36%
correct answers:0.86
