NAME=pythenv

YELLOW=\033[1m\033[93m
CYAN=\033[1m\033[96m
CLEAR=\033[0m

.PHONY: test

help:
	@echo "$(CYAN)help$(CLEAR)     Print this help page"
	@echo "$(CYAN)test$(CLEAR)     Run integration test"
	@echo "$(CYAN)release$(CLEAR)  Release project"

test:
	@echo "$(YELLOW)Running integration test$(CLEAR)"
	./pythenv -r test/requirements.txt test/script.py
	./pythenv test/script.py

release: test
	@echo "$(YELLOW)Releasing project$(CLEAR)"
	release
