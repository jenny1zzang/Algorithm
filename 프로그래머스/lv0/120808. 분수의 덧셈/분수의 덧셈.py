def solution(numer1, denom1, numer2, denom2):
    answer = []
    mcd = 1

    for i in range(1,min(denom1, denom2)+1):
        if denom1 % i == 0 and denom2 % i == 0:
            mcd = max(i,mcd)

    lcm = mcd * denom1//mcd * denom2//mcd


    answer.append(numer1 * (lcm//denom1) + numer2 * (lcm//denom2))
    answer.append(lcm)

    temp = 0
    for i in range(1, min(answer[0],answer[1])+1):
        if answer[0] % i == 0 and answer[1] % i == 0:
            temp = i

    answer = [a//temp for a in answer]

    return answer