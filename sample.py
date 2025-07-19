print('{0},{1},{2}'.format('apple','banana','carrot','pen'))
print('{},{},{}'.format('apple','banana','carrot'))
print('{2},{1},{0}'.format('apple','banana','carrot'))
print('{0},{1},{1},{0}'.format('apple','banana','carrot'))
print('{2},{1},{0}'.format(*'abcd'))
print('{0},{1},{0}'.format('apple','banana','carrot'))
print('coordinates:{latitude},{longitude}'.format(
    latitude='37.24N',longitude='-115.81w'))
print('welcome:{name},your college is:{college}'.format(
    name='vyshnavi',college='NIT'))
coord={'latitude':'37,24N','longitude':'-115.81W'}
print('coordinate:{latitude},{longitude}'.format(**coord))
c=3-5j
print('The complex number{0} is formed from the real\
part {0.real} and the imaginary part {0.imag}.'.format(c))
coord=(3,5)
abc=(2,9)
print('x:{0[0]};y:{0[1]};abc:{1[0]},{1[1]}'.format(coord,abc))
print('x:{0[0]};y:{0[1]};abc:{1[0]},{1[1]}'.format(coord,abc))
coord=[(3,9),(2,4)]
print('first tuple:{0[0]},{0[1]},second tuple:{1[0]}{1[1]}'.format(*coord))
course=['B.tech','M.tech','MBA','MCA']
print('''this college provides various courses.{0}
is of 4 years and {1} is of 2 years and {3} and {2} are of 2 years'''.format(*course))


#O/P:
apple,banana,carrot
apple,banana,carrot
carrot,banana,apple
apple,banana,banana,apple
c,b,a
apple,banana,apple
coordinates:37.24N,-115.81w
welcome:vyshnavi,your college is:NIT
coordinate:37,24N,-115.81W
The complex number(3-5j) is formed from the realpart 3.0 and the imaginary part -5.0.
x:3;y:5;abc:2,9
x:3;y:5;abc:2,9
first tuple:3,9,second tuple:24
this college provides various courses.B.tech
is of 4 years and M.tech is of 2 years and MCA and MBA are of 2 years

