PROJECT_PATH = ./src

optimize_imports:
	isort .

codestyle:
	flake8 $(PROJECT_PATH)