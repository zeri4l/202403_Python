
# 과제1
'''
a=5
b=1
c=3
a, b, c=b, c, a
print(a, b, c)
'''
#과제2
'''
a, b = map(int, input().split())
print(a+b)
'''
#과제3
'''
list=[0,1,2,3,4]
dict={'a': 'b'}
list.append(dict)
print(list)
'''
#과제4
'''
A=input().split()
A=set(A)
B=input()
print(B in A) 
'''

#과제5

a=1
b=3.2
c="string"
d={}
e=[]
f=()
g=set()
h=(10==10)
X="a, b, c, d, e, f, g, h"

# print(type(X.split()))
print('\n'.join(map(lambda K: str(type(eval(K))), X.split(", "))))
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
# print(type(h))
