n = int(input('카운트다운'))

#for num in range(n,0,-1):
    #print(num, end="")

s=1

while True:
    print(n, end=" ")
    n -= s
    if n == 0:
        break
