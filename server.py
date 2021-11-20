import socket
import threading

table={

    '192.168.1.1' : '1E.4A.4B.11',
    '192.168.0.1' : '1B:3c:4a:iD',
    '192.168.5.10': '3A:4c:5D:3e',
}
#ip=socket.gethostbyname(socket.gethostname())



s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',4444))

def handle_client(conn,addr):
    print(f'connection information:{addr}')
    connected  =  True
    while connected:
        msg=conn.recv(1024).decode()
        if msg:
            mac = table.get(msg)
            conn.send(mac.encode())
            if msg=='!disconnect':
                connected=False
    conn.close()

        

def start():
    s.listen()
    while True:
        conn , addr = s.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f'Active thread:{threading.activeCount()-1}')



print('Starting server..')
start()


# print("connection from:",addr)
# ip=addr.recv(1024)
# ip=ip.decode('UTF-8')
# mac=table.get(ip)
# addr.send(mac.encode())
