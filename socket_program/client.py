import socket
s = socket.socket()
try:
	s.connect(('www.google.com',80))
	print "connected"
except Exception as err:
	print err
finally:
	s.close()
