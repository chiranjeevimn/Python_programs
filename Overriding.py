import math
class square:
    def area(self,x):
        print("area of square is %.4f"%x*x)
class c(square):
    def area(self,x):
        print("area of circle is %.4f"%(math.pi*x*x))
a=c()
a.area(15)
