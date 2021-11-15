# Introduction 
This is a snippet to compactly test a function in python.  
This is a snippet purpose is to fast test your Python code.  
What this snippet does is to fetch your code file functions one by one and test them against test cases you specify.  
Test cases are data-based tests that assert the known inputs of a function will return expected outputs.
The snippet make use of `pytest ` package and test cases are expected to be in `config.yaml`

# Installation
> * Clone the repo...  
`$ git clone https://github.com/MagedMohamedTurk/Python-Test-Function.git`  
* Run the following to up to date with the required packages:  
`pip install requirement.txt`  


# USAGE  
Copy testmypy/ directory to your Python project:  
`$ cp testmypy/ yourWorkingProject/`  
`$ cd yourWorkingProject/testmypy/`  
Utilizing `makefile` to test your Python funcitons:  
>`$ make pre`  
Copying files to the working directory


>`$ make build`  
Building `config.yaml` file, collect all the python files. 
edit the config.yaml file to add testcases for the functions in the files.

>`$ make run`  
Run `pytest` to test the functions against the testcases you entered in the config.yaml.

>`$ make report`    
To make 'test_report.txt' file with the output.

>`$ make clean`  
To clean all the files added previously by the script.

TODO: Insert screenshots for illustrate the usage of the file 
