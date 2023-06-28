N, M = map(int, input().split())

cnt = 1
i = 0
while 1:
    if cnt == N*M:
        break
    i += 1
    cnt += 1
print(i)