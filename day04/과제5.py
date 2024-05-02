x= int(input('첫 번째 수를 입력'))
y= int(input('두 번째 수를 입력'))

if x<y:
    x,y = y,x
    

    
while True:
    if y==0 :
        print('최대공약수:', x)
        break
    
    else:
        r= x%y
        x=y
        y=r