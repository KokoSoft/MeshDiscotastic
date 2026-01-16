import sys
import logging

def error_exit(
	msg : str,
	logger : logging.Logger = logging,
	code : int = 1
):
	logger.critical(msg)
	sys.exit(1)