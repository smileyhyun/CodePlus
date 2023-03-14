N = int(input()) # 입력받을 숫자의 개수
num = list(map(int, input().split(' '))) # 공백으로 숫자 구분
count = 0 # 소수의 개수

for x in num:
  for i in range(2, x+1):
    if x % i == 0:
      if x == i:
        count += 1
      
      break

print(count)