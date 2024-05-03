import socket
while 1:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('10.130.171.194', 8085))
    client.send("I am CLIENT\n".encode())
    from_server = client.recv(4096)
    client.close()
    print (from_server.decode())
