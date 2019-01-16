#assn1 server program written by Steven Essig

import socket

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 12222)
sock.bind(server_address)
print("listening on: %s and port: %s" % server_address)

#Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    connection, client_address = sock.accept()
    print("Client Found! \n")
    print("Users take turns sending messages back and forth")
    print("The session will be closed if either user sends the message: Good bye my friend")
    print("The client goes first \n")
    print("Session is starting\n")

    try:

        # Receive the data and retransmit it back
        while True:
            data = connection.recv(256)
            decoded = data.decode()

            if 'Good bye my friend' in decoded:
                print("receiving: %s" % decoded)
                print("\nSession is closing")
                break
            # Echos back any data received that was not "Echo" or "Exit"
            else:
                print("receiving: %s" % decoded)
                data = input("sending: ")
                if 'Good bye my friend' in data:
                    connection.sendall(data.encode())
                    print("\nSession is closing")
                    break
                else:
                    connection.sendall(data.encode())
    finally:
        # Close up the connection and exit the server
        connection.close()
        exit()