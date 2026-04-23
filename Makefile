run:
	python app.py

test:
	pytest

doctest:
	python -m doctest -v validator.py

format:
	black .

lint:
	flake8 .

security:
	bandit -r . -x ./venv

check: format lint test doctest security