list=[]
n=map(int, input().split())
list.append(n)

sum=0
m=0 
for i in range(1,list[-1]+1):
    m= list[i]
    for j in range(1,n+1):
        sum+=(m//j)*j

print(sum)