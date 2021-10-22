import pytest
from collections import Counter
import yaml


# func_1 as example of single parameter function
def func_1(param):
    ""
    # Uncomment the following line to debug the function
    # import pudb; pudb.set_trace()
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
    import pudb; pudb.set_trace()
    required = {}
    for i in range(len(numbers)):
        if target - numbers[i] in required.keys():
            return (required[target - numbers[i]], i)
        else:
            required[numbers[i]] = i


# Testing Unit
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

# Loading test_cases for different functions
func_1_test_cases = {k: tuple(v) for k, v in
                     config['func_1']['test_cases'].items()}
two_sum_test_cases = {k: tuple(v) for k, v in
                     config['two_sum']['test_cases'].items()}


# Testing func_1 against its testcases
@pytest.mark.parametrize('param, expected', func_1_test_cases.values(),
                         ids=list(func_1_test_cases.keys()))
def test_func_1(param, expected):
    "Test for func()"
    print(40*'*')
    print('Input = ', param)
    print(40*'*')
    assert func_1(param) == expected


# Testing two_sum function against its testcases
@pytest.mark.parametrize('param, expected', two_sum_test_cases.values(),
                         ids=list(two_sum_test_cases.keys()))
@pytest.mark.timeout(0.5)
def test_two_sum(param, expected):
    "TEST FOR FUNC()"
    print(40*'*')
    print('Input = ', param)
    print(40*'*')
    assert two_sum(*param) == expected   # '*' should be included if
                                       # more than one parameter passed.


