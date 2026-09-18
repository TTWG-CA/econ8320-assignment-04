class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary
        
    def conjugate(self):
        return ComplexNumber(self.real, -1*self.imag)
    
    def __abs__(self):
        return (self.real**2 + self.imag**2)**0.5
    
    def __lt__(self, other):
        if abs(self)<abs(other):
            return True
        else:
            return False
        
    def __gt__(self, other):
        if abs(self)>abs(other):
            return True
        else:
            return False
        
    def __eq__(self, other):
        if (self.real==other.real) & (self.imag==other.imag):
            return True
        else:
            return False
        
    def __ne__(self, other):
        return not self==other

    def __add__(self,other): 
        return ComplexNumber(
            self.real + other.real, 
            self.imag + other.imag
        )

    def __sub__(self, other): 
        return ComplexNumber(
            self.real-other.real,
            self.imag - other.imag
        )
    def __mul__(self, other):
        real = self.real * other.real - self.imag*other.imag
        imag= self.real*other.imag + self.imag*other.real
        return ComplexNumber(real, imag)
    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real,imag)
    