n=int(input())
sum=0
for i in range(1,n+1):
    sum+=(n//i)*i
    #i의 배수의 개수 = i를 약수로 갖는 수
print(sum)