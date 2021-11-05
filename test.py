import pytest
import yaml
import code_file
from code_file import *
from inspect import getmembers, isfunction

# Loading config.yaml
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)
    # Loading global parameters
    timeout = config['timeout']

funcs = [func[0] for func in getmembers(code_file) if isfunction(func[1])]
print(funcs)


# Loading test_cases for different functions
''' TODO reconstruct the test_cases to do one dict with three values each
(param, expected, func)
then with no for loop we can parametrize over the three values'''
func_test_cases = []
for func in funcs:
    func_test_cases.extend(list((*v, func) for _, v in
                                       config[func]['test_cases'].items()))
    #import pudb; pudb.set_trace()

# TODO Fix: solve the problem of late binding
@pytest.mark.parametrize('param, expected, func',
                        func_test_cases,
                         )
def test(param, expected, func):
    print(param, expected, func)
    try:
        assert eval(func + '(*param) == expected')
    except TypeError:
        assert eval(func + '(param) == expected')


print(func_test_cases[0])



## Testing func_1 against its testcases
#@pytest.mark.parametrize('param, expected', func_1_test_cases.values(),
#                         ids=list(func_1_test_cases.keys()))
#def test_func_1(param, expected):
    #    "Test for func()"
    #    print(40*'*')
    #    print('Input = ', param)
    #    print(40*'*')
    #    try:
        #        assert func_1(param) == expected
        #    except TypeError:
            #        assert func_1(*param) == expected
            #
            #
            ## Testing two_sum function against its testcases
            #@pytest.mark.parametrize('param, expected', two_sum_test_cases.values(),
            #                         ids=list(two_sum_test_cases.keys()))
            #@pytest.mark.timeout(timeout)
            #def test_two_sum(param, expected):
                #    "TEST FOR FUNC()"
                #    print(40*'*')
                #    print('Input = ', param)
                #    print(40*'*')
                #    try:
                    #        assert two_sum(param) == expected
                    #    except TypeError:
                        #        assert two_sum(*param) == expected   # '*' should be included if
                        #        # more than one parameter is inserted
