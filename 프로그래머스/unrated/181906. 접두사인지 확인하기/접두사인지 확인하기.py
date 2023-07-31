def solution(my_string, is_prefix):
    prefix = []
    for i in range(len(my_string)):
        prefix.append(my_string[:i])
    
    for p in prefix:
        if is_prefix == p:
            return 1
    return 0