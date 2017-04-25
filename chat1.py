
import socket
import ssl
import pprint
import sys
import os
import thread
import time

def client_thread():
	sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock1.bind(('',5001))
	sock2 = ssl.wrap_socket(sock1,keyfile="www.example.com.key.pem",certfile="www.example.com.cert.pem",ca_certs="ca-chain.cert.pem", server_side = True)
	sock2.listen(5)
	conn, addr = sock2.accept()
	while True:
		msg = conn.recv(1024)
		print "Message received from ", addr,"is : ",msg 
		if msg == "-1":
			conn.close()
			os._exit(1)

thread.start_new_thread(client_thread,())
time.sleep(12)
servers = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = ssl.wrap_socket(servers, ca_certs="ca-chain.cert.pem",server_side = False , cert_reqs = ssl.CERT_REQUIRED)
addr = ('54.145.184.6', 5003)
sock2.connect(addr)
print "We are Connected to: ",addr
while True:
	sent_msg = raw_input("") 
	sock2.send(sent_msg)  
	if sent_msg=="-1" :
		sock2.close()
		sys.exit()		