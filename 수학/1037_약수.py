n=int(input())
list=list(map(int, input().split()))
list.sort() #리스트로 정렬
print(list[0]*list[n-1]) # 가장 큰 값과 가장 작은 값을 곱해줌