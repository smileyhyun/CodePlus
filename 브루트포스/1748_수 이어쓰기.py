N = input()
N_len = len(N) - 1
c = 0
i = 0
while i < N_len:
    c += 9 * (10 ** i) * (i + 1)
    i += 1
c += ((int(n) - (10 ** N_len)) + 1) * (N_len + 1)
print(c)