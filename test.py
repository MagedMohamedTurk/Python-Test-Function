from inspect import getmembers, isfunction
import pytest
import yaml
import importlib

# Loading config.yaml
try:
    with open('config.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        # Loading global parameters
        timeout = config['timeout'] #TODO check time to be a number
        mod = config['code_file']
except (yaml.YAMLError, IOError):
    print('Error loading <config.yaml> file')

mod_file = importlib.import_module(mod)
# Import only functions from the files
globals().update({name: value for name, value in mod_file.__dict__.items()
                if callable(value)})
# Get functions names
funcs = [func[0] for func in getmembers(mod_file) if isfunction(func[1])]
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
