#SOCKETS --------------------------------
from time import sleep

# Sockets are a way of sending data over a network.
# There are two main types of sockets, TCP and UDP.
import socket

# To make a connection to a TCP server:
# AF_INET: connecting to an IPv4 IP;  SOCK_STREAM: connecting over TCP and not UDP.
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('127.0.0.1', 9987))
# Send data
clientsocket.send('hello')
# Receive data. Pass max number of bytes of data to accept
data = clientsocket.recv(1024)
print(data)

# To make a TCP Server:
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to listen to a port.
serversocket.bind(("127.0.0.1", 9985))
# Tell the socket to start listening; Pass the maximum number of connections.
serversocket.listen(10)

# Setup an infinite loop so the socket will keep listening for incoming connections.
while True:
    # If it gets a new connection, accept it and save the connection and address.
    connection, address = serversocket.accept()
    # Read 1024 bytes of data from the connection.
    data = connection.recv(1024)
    # Check the length of data. If the length is more than 0 then
    # that means something was sent, so print it out.
    if len(data) > 0:
        print("Received: " + data)
    connection.close()
    break
serversocket.close()
sleep(0.05)
