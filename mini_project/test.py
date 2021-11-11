import importlib
from inspect import getmembers, isfunction
import pytest
import yaml


# Loading config.yaml
try:
    with open('config.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        # Loading global parameters
        timeout = config['timeout']  # TODO check time to be a number
        # get all files in config.yaml
        files = config['code_file']
except (yaml.YAMLError, IOError):
    print('Error loading <config.yaml> file')
funcs = []
# Iterate through all files to get list of functions
for module in files:
    mod_file = importlib.import_module(module)  # Import the module
    # Import only functions from the files
    globals().update({name: value for name, value in mod_file.__dict__.items()
                      if callable(value)})
    # Get functions names from all modules
    funcs.extend([func[0] for func in getmembers(mod_file)
                  if isfunction(func[1])])


# TODO remove function if test case is not available
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
