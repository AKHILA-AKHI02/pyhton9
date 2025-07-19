mo=open(r"D:\mca_test\vy.txt","wt")
count=0
while count<5:
    str1=input("Enter text:")
    mo.write(str1+'\n')
    count=count+1
mo.close()
print("work done")
