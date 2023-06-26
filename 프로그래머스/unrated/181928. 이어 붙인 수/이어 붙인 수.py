def solution(num_list):
    even = 0
    odd = 0
    for i in num_list:
        if i % 2 == 1:
            if even == 0:
                even += i
            else:
                even = even*10 + i
        else:
            if odd == 0:
                odd += i
            else:
                odd = odd*10 + i
            
    return even + odd