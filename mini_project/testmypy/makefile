MAKEFLAGS += --silent
help:
	echo 'Testmypy snippet will test functions in your project py function\
		snippet assume this folder is sub folder for the project to be tested (includes .py files)\
		make sure that project directory does not have similiare test.py files'
	echo 'make pre --> copying test.py and build_config.yaml to working directory'
	echo 'make build --> collect py files from working directory and construct config.yaml file\
		You need to enter the testcases one by one and write your function names by hand\
		if the name of the function is not the same as in the .py file it will be ignored in the test'
	echo 'make report  --> make a test_report.txt file for the lattest test'
	echo 'make clean  --> remove all files that has been created by (make pre)'
pre:
	echo 'Copy test.py - build_config.py files to directory';\
	cp test.py build_config.py ../
build:
	cd ../;	echo 'Build config.yaml file';\
	python build_config.py; echo 'Now, please add testcases to your new config.yaml file'
	
run:
	cd ../; echo 'Run pytest';\
	pytest -v test.py
report: # Bug Error 1 but create the file successfully
	cd ../; echo 'Make a report';\
	pytest -v test.py > test_report.txt
clean:
	cd ../; echo 'Clean';\
	rm -r test.py build_config.py config.yaml __pycache__/ 
