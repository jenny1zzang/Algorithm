def solution(num_list):
    s = 0
    m = 1
    answer = 0
    for i in num_list:
        m *= i
        s += i
        
    s = s**2
    if s < m:
        answer = 0
    else: answer = 1
    return answer