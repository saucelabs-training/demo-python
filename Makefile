run:
	rm -rf result_log.txt && touch result_log.txt
	LOG_OUTPUT=true py.test -n 10 tests
	cat result_log.txt
