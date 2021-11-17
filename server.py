import socket

table={

    '192.168.1.1' : '1E.4A.4B.11'
}


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',4444))
s.listen()
address=s.accept()
print("connection from:",address)
ip=address[0].recv(1024)
ip=ip.decode('UTF-8')
mac=table.get(ip)
address[0].send(mac.encode())
