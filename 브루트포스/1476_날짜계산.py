import sys
input=sys.stdin.readline

#1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19
E, S, M = map(int, input().split())
e, s, m = 1, 1, 1
year = 1

while True:
    if e == E and s == S and m == M:
        print(year)
        break
    e =e + 1
    s = s+ 1
    m = m + 1

#범위를 넘어갈 경우 1로 바꿔줌
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1
    year += 1