def solution(array):
    cnt = [0] * (max(array)+1)
    
    for i in array:
        cnt[i] += 1
    
    max_cnt = 0
    for i in cnt:
        if i == max(cnt):
            max_cnt += 1
    if max_cnt == 1:
        return cnt.index(max(cnt))
    else :
        return -1