def solution(intStrs, k, s, l):
    x = []
    for i in range(len(intStrs)):
        tmp = intStrs[i]
        x.append(int(tmp[s:s+l]))
    
    answer = []
    for i in range(len(x)):
        if x[i] > k :
            answer.append(x[i])
    return answer
    