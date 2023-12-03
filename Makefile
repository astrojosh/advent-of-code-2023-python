run:
	@python -m tests.test_day_$(day)

test:
	@pytest tests/test_day_$(day).py -k "$(part)"
