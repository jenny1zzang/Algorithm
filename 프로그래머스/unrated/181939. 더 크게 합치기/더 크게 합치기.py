def solution(a, b):
    a_str = str(a)
    b_str = str(b)
    if (int(a_str+b_str) < int(b_str+a_str)):
        return int(b_str+a_str)
    else:
        return int(a_str+b_str)