def solution(numLog):
    word = ""
    for i in range(len(numLog)-1):
        if numLog[i+1]-numLog[i] == 1:
            word+="w"
        elif numLog[i+1]-numLog[i] == -1:
            word+="s"
        elif numLog[i+1]-numLog[i] == 10:
            word+="d"
        elif numLog[i+1]-numLog[i] == -10:
            word+="a"
    return word