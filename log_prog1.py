import logging
logging.basicConfig(filename="log1.txt",
					level=logging.DEBUG,
					format="%(asctime)s<->%(levelname)s<->%(message)s")
import log_module
log_module.fun1()

logging.info("......................program started.........................")
def fun():
	logging.info("Function started")
	a=100
	b=200
	c=a+b
	logging.info("Function ended with retur value:{0}".format(c))
	return c
a=raw_input("Enter a value:")
if not a.isdigit():
	logging.warn('a should be digit only')
b=raw_input("Enter b value:")
if not b.isdigit():
	logging.warn('b should be digit only')
if b==0:
	logging.warn('will get an exception')
try:
	a=int(a)
	b=int(b)
	print a/b
except Exception as err:
	logging.exception(err)
logging.info("program ended")


