def solution(my_string, is_suffix):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[-i:])
    
    for i in answer:
        if i == is_suffix:
            return 1
    return 0