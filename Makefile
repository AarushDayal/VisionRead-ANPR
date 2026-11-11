.PHONY: check

check:
	./venv/bin/python -m pytest tests -q
