PROJECT=PassGen
VENV=$(HOME)/.virtualenvs/$(PROJECT)


venv:
	python3 -m venv $(VENV)


install:
	pip install -r requirements.txt
