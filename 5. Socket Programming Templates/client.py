import socket 
s = socket.socket()
s.connect(('127.0.0.1',9999))

send = ''
while send != 'end':
    send = input("enter message: ")
    sendB = send.encode()
    s.sendall(sendB)
    recv = s.recv(1024)
    print(f"received: {recv.decode()}")

    if recv == b'end':
        break

s.close()
print('connection closed')