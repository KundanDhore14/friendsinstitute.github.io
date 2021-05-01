class Complexnumber:
    def __init__(self,r,i):
        self.real =r 
        self.imaginery = i

    def __add__(self,c):
        return Complexnumber(self.real +c.real,self.imaginery+c.imaginery)
    
    def __mul__(self,c):
        mulReal = self.real*c.real - self.imaginery*c.imaginery
        mulImg = self.real*c.imaginery + self.imaginery*c.real
        return Complexnumber(mulReal,mulImg)

    def __str__(self):
        if self.imaginery<0:
            return f"{self.real}-{-self.imaginary}"
        else:
            return f"{self.real} + {self.imaginery}i"
c1 = Complexnumber(1,4)
c2 = Complexnumber(8,4)
print(c1+c2)
print(c1*c2)