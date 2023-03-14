import sys
N = int(sys.stdin.readline()) #이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)
M = int(sys.stdin.readline()) #고장난 버튼의 개수 M (0 ≤ M ≤ 10)
broken = list(map(str, sys.stdin.readline().split())) #고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어짐
x = abs(100 - N) # 리모컨을 눌러야하는 최대 개수(절댓값 함수)

# 반복문을 통해 이동해야하는 채널로 가기 위한 방법 확인
for i in range(1000001):

    # 반복문을 통해 채널로 이동하기 위해 눌러야 하는 번호가 고장이 났는지 확인
    for j in str(i):
        if j in broken:
            break

    # 채널로 이동 가능하다면 원래 x와 채널을 누른 개수와 +/- 를 누른 개수를 x에 담는다.
    else:
        x = min(x, len(str(i)) + abs(i - N))

print(x)