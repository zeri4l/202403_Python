# index에서 end는 포함하지 않음
# copy를 쓰면 리스트가 연동되지 않음. 그러나 내부의 리스트는 연동
# append는 리스트 포맷 자체가, extend는 리스트 내부 요소가
# 튜플은 리스트와 비슷하지만 값 변경 불가 tu=(1,)
# sort는 원본에 영향, sorted는 원본 변화x
# key:value 형태, key는 변경 불가
# 빈 집합은 set()
# 집합은 같은 값이 없도록 자동 조절

# A=map(int, input().split())
A=input().split()
A=str(A)
# A=int(A)
B=input()
# B=int(B)
print(B in A) 