def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        min = 1000001
        for i in range(len(arr)):
            if i>=s and i<=e and arr[i]>k and min > arr[i]:
                    min = arr[i]
        if min == 1000001:
            answer.append(-1)
        else:
            answer.append(min)
    return answer