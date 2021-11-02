from collections import Counter


# func_1 as example of single parameter function
def func_1(param):
    ""
    # Uncomment the following line to debug the function
    #import pudb; pudb.set_trace()
    score = 0
    counter = Counter(param)
    if counter[1] >= 3:
        score += 1000
        for _ in range(3): param.remove(1)
    elif counter[6] >= 3:
        score += 600
        for _ in range(3): param.remove(6)
    elif counter[5] >= 3:
        score += 500
        for _ in range(3): param.remove(5)
    elif counter[4] >= 3:
        score += 400
        for _ in range(3): param.remove(4)
    elif counter[3] >= 3:
        score += 300
        for _ in range(3): param.remove(3)
    elif counter[2] >= 3:
        score += 200
        for _ in range(3): param.remove(2)
    while Counter(param)[1] >= 1:
        score += 100 
        param.remove(1)
    while Counter(param)[5] >= 1:
        score += 50 
        param.remove(5)
    return score


# two_sum as example of multiple parameters function
def two_sum(numbers, target):
    #import pudb; pudb.set_trace()
    required = {}
    for i in range(len(numbers)):
        if target - numbers[i] in required.keys():
            return (required[target - numbers[i]], i)
        else:
            required[numbers[i]] = i

