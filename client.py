import socket


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('localhost',4444))
connected = True
while connected:
    ip=input("Enter IP:")
    s.send(ip.encode())
    mac=s.recv(1024)
    mac=mac.decode()
    print("mac address:", mac)
    ips=input('Do you want to continue: y or n :')
    if ips =='n':
        s.send('!disconnect').encode()
    else:
        continue 
