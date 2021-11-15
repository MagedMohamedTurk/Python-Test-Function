import ruamel.yaml
import os
# get the path of the current directory
path = os.getcwd()
# Check if file exists
while os.path.exists('trythisconfig.yaml'):
    warning = input('Warning!! file already exists. Do you want to Overwrite?(Y-n)')
    if warning.lower() in ['n', 'no']:
        exit()
    elif warning.lower() in ['y', 'yes', '']:
        break
    else:
        print('Please enter (Y-n)')
        continue
directories = os.listdir(path)
# This would print all the files and directories
pyfiles = []
for file in directories:
    if file.endswith('.py') and file not in ['build_config.py', 'test.py']:
        pyfiles.append(file[:-3])

yaml_str = """\

# Global parameters
timeout : 0.5  # Time that cause timeout for functions

# Check mini-project folder for examples
# Uncomment to write the name of your code files
# List all code files here without .py extension
code_file :


######################################################################
# Test Case Format
# function name: (as in the code file)
#   test_cases: (always the same)
#       'test_case_1': (can be renamed anything between '')
#           - Input parameters (multiple paramters should be in a list [])
#           - Expected output  (exmaple for tuple >> !!python/tuple [1, 2])
######################################################################

# Uncomment to write your function test cases.

#func_1:
#    test_cases :
#        'test_case_1':
#                - [2, 3, 4, 6, 2]
#                - 0
#        'test_case_2':
#                - [4, 4, 4, 3, 3]
#                - 400
#
"""

yaml = ruamel.yaml.YAML()  # defaults to round-trip if no parameters given
code = yaml.load(yaml_str)
code['code_file'] = pyfiles
with open('trythisconfig.yaml', 'w') as f:
    yaml.dump(code, f)
