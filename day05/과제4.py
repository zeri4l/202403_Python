PI = 3.141592

r=int(input("반지름"))
def S(r):
    global PI
    print(PI*r**2)
    
def L(r):
    global PI
    print(2*PI*r)
    
S(r)
L(r)