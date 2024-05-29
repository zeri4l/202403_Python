class D:
    def __init__(self, d):
        self.d = d

class C(D):
    def __init__(self, c, d):
        self.c = c
        super().__init__(d) 

class B(C):
    def __init__(self, b, c, d):
        self.b = b
        super().__init__ (c, d)

class A(B):
    def __init__(self, a, b, c, d):
        self.a = a
        super().__init__(b, c, d)  
        
    def __str__(self) -> str:
        return f"{self.a}, {self.b}, {self.c}, {self.d}"

e = A(1,2,3,4)
print(e)
