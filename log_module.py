import logging

def fun1():
	logging.info("function started in log_module{0}".format(__name__))
	logging.info("Function ended in log_module")