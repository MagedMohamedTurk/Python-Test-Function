from inspect import getmembers, isfunction
import pytest
import yaml
import code_file
from code_file import *


# Loading config.yaml
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    # Loading global parameters
    timeout = config['timeout']

# Get functions names
funcs = [func[0] for func in getmembers(code_file) if isfunction(func[1])]
print(funcs)

# TODO test if config.yaml is missing or bad formatted
# Loading test_cases for different functions
func_test_cases = []
for func in funcs:
    func_test_cases.extend(list((*v, func) for _, v in
                           config[func]['test_cases'].items()))


@pytest.mark.parametrize('param, expected, func',
                         func_test_cases,
                         ids=list(item[-1]+' Case# :' for item in
                         func_test_cases)
                         )
@pytest.mark.timeout(timeout)
def test(param, expected, func):
    try:
        assert eval(func + '(*param) == expected')
    except TypeError:
        assert eval(func + '(param) == expected')
