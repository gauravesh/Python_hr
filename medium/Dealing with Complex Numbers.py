import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
        
   
    def __add__(self, no):
        add_r = self.real+no.real
        add_s = self.imaginary+no.imaginary
        return Complex(add_r,add_s)
        
    def __sub__(self, no):
        sub_r = self.real-no.real
        sub_s = self.imaginary-no.imaginary
        return Complex(sub_r,sub_s)
        
    def __mul__(self, no):
        mult_r = self.real*no.real-self.imaginary*no.imaginary
        mult_s = self.real*no.imaginary+self.imaginary*no.real
        return Complex(mult_r,mult_s)

    def __truediv__(self, no):
        denominator= pow(no.real,2)+pow(no.imaginary,2)
        div_r = self.real*no.real + self.imaginary*no.imaginary
        div_s = self.imaginary * no.real - self.real*no.imaginary
        return Complex((div_r/denominator),(div_s/denominator))


    def mod(self):
        return Complex (math.sqrt((pow(self.real,2) + pow(self.imaginary,2))),0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
