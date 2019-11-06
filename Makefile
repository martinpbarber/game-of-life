VENV_DIR := .venv
VENV_BIN := $(VENV_DIR)/bin
REQUIREMENTS := requirements.txt
REQUIREMENTS_MARKER := .$(REQUIREMENTS)

.PHONY: test init clean

test: init
	$(VENV_BIN)/python -m pytest tests/
	#$(VENV_BIN)/pytest tests

init: $(VENV_DIR) $(REQUIREMENTS_MARKER)

$(VENV_DIR):
	python3 -m venv $(VENV_DIR)
	$(VENV_BIN)/pip install --upgrade pip
	$(VENV_BIN)/pip install --upgrade setuptools
	$(VENV_BIN)/pip install --upgrade wheel

$(REQUIREMENTS_MARKER):
	$(VENV_BIN)/pip install -r $(REQUIREMENTS) && touch $(REQUIREMENTS_MARKER)

clean:
	rm -rf $(VENV_DIR)
	rm -f $(REQUIREMENTS_MARKER)
	rm -rf .pytest_cache
	find . -type d -name '__pycache__' -exec rm -rf {} \;

