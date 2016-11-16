import socket
import json
host = socket.gethostname()
port = 8889
s=socket.socket()
try:
	s.connect((host,port))
	ack = s.recv(1024)
	print ack
	a=raw_input("Enter person id")
	s.send(a)
	resp = s.recv(1024)
	print resp,type(resp)
	resp = json.loads(resp)
	print resp,type(resp)
	for i in resp:
		print i
except Exception as err:
	print err
finally:
	s.close()