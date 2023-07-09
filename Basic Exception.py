try:
    f=open("b",'w')
    a,b=[int(j) for j in input("enter the two numbers").split()]
    c=a/b
    f.write("writing %d into the file"%c)
except ZeroDivisionError:
    print("d b z e")
    print("zero can not be divided")
finally:
    f.close()
    print("file closed")
    
