import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12222)
sock.connect(server_address)

print("connecting to %s port %s" % server_address)
print("\nUsers take turns sending messages back and forth")
print("The session will be closed if either user sends the message: Good bye my friend")
print("The client goes first \n")
print("Session is starting\n")

while True:

    message = input("sending: ")
    sock.sendall(message.encode())

    if 'Good bye my friend' in message:
        print("\nSession is closing")
        break

    else:
        data = sock.recv(256)
        if 'Good bye my friend' in data.decode():
            print("receiving: %s" % data.decode())
            print("\nSession is closing")
            break

        else:
            print("receiving: %s" % data.decode())

print("closing socket")
sock.close()
