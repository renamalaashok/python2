import socket
import db
host = socket.gethostname()
port = 8889
try:
	s = socket.socket()
	s.bind((host,port))
	s.listen(6)
	print "Waiting for the clinet request"
	client_obj,client_info = s.accept()
	client_obj.send("Connected successfully!!!")
	clinet_data = int(client_obj.recv(1024))
	res = db.browse(clinet_data)
	'''
	res="ODD"
	if clinet_data%2==0:
		res = "EVEN"
	'''
	client_obj.send(res)
except Exception as err:
	print err
finally:
	s.close()