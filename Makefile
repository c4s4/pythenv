# Makefile for project continuum

# Parent makefiles at https://github.com/c4s4/make
include ~/.make/Python.mk

itg: # Run integration test
	@echo "$(YEL)Running integration test$(END)"
	$(PYTHON) pythenv -r test/requirements.txt test/script.py
	$(PYTHON) pythenv test/script.py
