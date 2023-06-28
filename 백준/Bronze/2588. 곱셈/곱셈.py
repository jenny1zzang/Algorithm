a = int(input())
b = int(input())

answer = []

while b > 0:
    answer.append(a*(b%10))
    b //=10

s = 0
for i in range(len(answer)):
    print(answer[i])
    s += answer[i]*(10**i)

print(s)