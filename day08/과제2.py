import random

def lotto():
    a = int(random.randint(1,45))
    b = int(random.randint(1,45))
    if b == a:
        b = int(random.randint(1,45))
    c = int(random.randint(1,45))
    if c == a:
        int(random.randint(1,45))
    elif c == b:
        int(random.randint(1,45))
    d = int(random.randint(1,45))
    if d == a:
        int(random.randint(1,45))
    elif d ==b:
        int(random.randint(1,45))
    elif d == c:
        int(random.randint(1,45))
    e = int(random.randint(1,45))
    if e == a:
        int(random.randint(1,45))
    elif e ==b:
        int(random.randint(1,45))
    elif e == c:
        int(random.randint(1,45))
    elif e == d:
        int(random.randint(1,45))
    f = int(random.randint(1,45))
    if f == a:
        int(random.randint(1,45))
    elif f ==b:
        int(random.randint(1,45))
    elif f == c:
        int(random.randint(1,45))
    elif f == d:
        int(random.randint(1,45))
    elif f == e:
        int(random.randint(1,45))
    print(a,b,c,d,e,f)
        
lotto()
    