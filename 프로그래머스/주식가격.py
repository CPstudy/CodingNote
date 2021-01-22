def solution(prices):
    answer = []
    for i in range(len(prices)): 
        check_num = 0 
        for j in range(i+1, len(prices)):
            check_num = check_num + 1
            if prices[i] > prices[j]: 
                break 
        answer.append(check_num) 
    return answer