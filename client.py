import socket


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('localhost',4444))
ip=input("Enter IP:")

s.send(ip.encode())
mac=s.recv(1024)
mac=mac.decode()
print("mac address:", mac)
