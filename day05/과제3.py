i=2
k=int(input())

while i<k:
    is_prime = lambda i,k : k%i
    a = int(is_prime(2, k))
    if a != 0:
            print(str(k) + "는 소수입니다.")
            break
    elif a == 0:
            print(str(k) + "는 소수가 아닙니다.")
            break
    
    else:
            i+=1
            
    
    
        