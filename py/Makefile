VENV = venv
PYTHON = $(VENV)/bin/python3
PIP= $(VENV)/bin/pip
TESTS = tests/*.py

activate:
	(
		source ./venv/bin/activate &&
		pip install -r requirements.txt
	)


run:
	python3 ./main.py

clean:
	rm -rf __pycache__

test:
	$(PYTHON) -m pytest $(TESTS)

fmt:
	

	