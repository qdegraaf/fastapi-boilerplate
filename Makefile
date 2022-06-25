.PHONY: clean, install, requirements, test, coverage, format, lint, docs

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	find . -name '*.egg-info' | xargs rm -rf

install:
	pip install -r requirements_dev.txt


requirements:
	pip install pip-tools
	pip-compile

# Testing
test:
	py.test tests/

coverage:
	pytest --cov=app

# Formatting & Code strength
format:
	black app/ tests/ setup.py app.py
	isort app tests setup.py app.py


lint:
	flake8 & mypy --config-file=mypy.ini .
