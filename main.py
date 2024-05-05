from Serial import *
import time
import subprocess
import socket
import serial
devices= ["/dev/ttyACM0","/dev/ttyACM1"]

ser=attempt_connection(devices)

host = '10.20.2.162'
port = 12345

def connect_socket(host,port):
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,port))
	return s


def process(command):
	client_socket=connect_socket(host,port)
	subprocess_instance=None
	if command=="SystemOn":
		subprocess_instance=subprocess.Popen(["/home/anon/miniconda3/envs/yolov8_picam/bin/python", "/home/anon/projects/Monkey/New/nogui.py"])
	elif (command=="SystemOff" ) and subprocess_instance is not None:
		subprocess_instance.terminate()
		subprocess_instance = None
	elif command == "UnlockAll":
		client_socket.sendall("UnlockAll".encode())
	elif command == "LockAll":
		client_socket.sendall("LockAll".encode())
	elif command == "Lock1":
		client_socket.sendall("Lock1".encode())
	elif command == "Unlock1":
		client_socket.sendall("Unlock1".encode())
	elif command == "Lock2":
		client_socket.sendall("Lock2".encode())
	elif command == "Unlock2":
		client_socket.sendall("Unlock2".encode())
	elif command == "Boff":
		client_socket.sendall("Boff".encode())
	client_socket.close()

try:	
	while True:
		command=read_serial_response(ser)
		print(command)
		process(command)
		time.sleep(0.1)
finally:
	if client_socket is not None:
		client_socket.close()
	if subprocess_instance is not None:
		subprocess_instance.terminate()


client_socket.close()
