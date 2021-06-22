import socket
mysocket = socket.socket()
mysocket.bind(('127.0.0.1', 9999))
mysocket.listen()

mysocket, address = mysocket.accept()
print(f"mysocket: {mysocket}, address: {address}")
# prints mysocket: <socket.socket fd=364, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0,laddr=('127.0.0.1', 9999), raddr=('127.0.0.1', 1087)>, address: ('127.0.0.1', 1087)

data = b''
send = ''

while send != 'end':
    # while b'\n' not in data:
    data = mysocket.recv(1024)
    # this while loop is good practice, so that like when the client side crashes, it cannot just like continually send empty strings. but honestly not necessary as well - since i am only expecting a single response from the other side. by using \n as the end of the data, it also ensures even blank messages are being sent over
    print(f"received: {data.decode()}")
    
    if data == b'end':
        break
    send = input("enter message: ")
    mysocket.sendall(send.encode())

print('connection closed')
