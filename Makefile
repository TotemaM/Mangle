NAME	= main.py
CC		= python3
SRCD	= src

all:
	$(CC) $(SRCD)/$(NAME)

production:
	$(CC) $(SRCD)/$(NAME) $@

.PHONY: update

update:
	pip install -r requirements.txt
