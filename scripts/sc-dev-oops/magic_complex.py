class Complex: 
    def __init__(self, imag: float, real: float = 0.0) -> None: 
        self.real = real 
        self.imag = imag 
        
    def __add__(self, __other): 
        if isinstance(__other, (float, int)):
            __other = Complex(real = __other, imag=0.0) 
            return Complex(imag=self.imag + __other.imag, real=self.real + __other.real) 
        
    def __radd__(self, __other): 
        return self.__add__(__other) 
        
    def __sub__(self, __other): 
        if isinstance(__other, (float, int)): 
            __other = Complex(real = __other, imag=0.0) 
            return Complex(imag=self.imag - __other.imag, real=self.real - __other.real) 
        
    def __rsub__(self, __other): 
        if isinstance(__other, (float, int)): 
            __other = Complex(real = __other, imag=0.0) 
            return __other.__sub__(self) 
        
    def __neg__(self): 
        return Complex(real = -self.real, imag = -self.imag) 
    
    def __mul__(self, __other): 
        return Complex(real = self.real*__other.real - self.imag*__other.imag,
                        imag = self.imag * __other.real + self.real*__other.imag) 
    
    def __str__(self): 
        return f"{self.real} + ({self.imag})*i" 
    
    def __repr__(self) -> str: 
        return f"Complex({self.real}, {self.imag})" 
    
z1 = Complex(real=2, imag=3) 
z2 = Complex(real=1, imag=2) 
print(z1 + z2) 
print(z1 - z2)
z1 = Complex(real=2, imag=3) 
z2 = Complex(real=1, imag=-4) 
print(z1 * z2) 
print(-z1) 
print(z1 + 1) 
print(1 + z1)
print(z1 - 1) 
print(1 - z1)
