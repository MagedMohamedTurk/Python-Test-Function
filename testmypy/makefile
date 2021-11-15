MAKEFLAGS += --silent
pre:
	echo 'Copy file to directory';\
	cp test.py build_config.py ../
build:
	cd ../;	echo 'Build config.yaml file';\
	python build_config.py
	
run:
	cd ../; echo 'Run pytest';\
	pytest -v test.py
report:
	cd ../; echo 'Make a report';\
	pytest -v test.py > test_report.txt
clean:
	cd ../; echo 'Clean';\
	rm -r test.py build_config.py config.yaml __pycache__/ 
