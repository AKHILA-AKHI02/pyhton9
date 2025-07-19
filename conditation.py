mo=open(r"D:\mca_test\mouni.txt","a")
while True:
    str1=input("Enter text:")
    mo.write(str1+'\n')
    choice=input("To exit type x:")
    if choice=='x' or choice=='X':
        break
    else:
        continue
mo.close()
print("work done")


#o/p:
Enter text:mounika
To exit type x:mamatha
Enter text:mahalakshmi
To exit type x:X
work done
