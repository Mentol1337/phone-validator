run:
	python app.py

test:
	pytest

format:
	black .

lint:
	flake8 .