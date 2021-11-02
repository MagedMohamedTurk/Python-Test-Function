import pytest
import yaml
from code_file import *


# Loading config.yaml
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

timeout = config['timeout']
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
    try:
        assert func_1(param) == expected
    except TypeError:
        assert func_1(*param) == expected


# Testing two_sum function against its testcases
@pytest.mark.parametrize('param, expected', two_sum_test_cases.values(),
                         ids=list(two_sum_test_cases.keys()))
@pytest.mark.timeout(timeout)
def test_two_sum(param, expected):
    "TEST FOR FUNC()"
    print(40*'*')
    print('Input = ', param)
    print(40*'*')
    try:
        assert two_sum(param) == expected
    except TypeError:
        assert two_sum(*param) == expected   # '*' should be included if
        # more than one parameter is inserted
