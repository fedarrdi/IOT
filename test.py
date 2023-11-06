import socket


# Define the host and port to listen on
host = '0.0.0.0'  # Listen on all available network interfaces
port = 8000  # Change this to the desired port

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections (up to 5 simultaneous clients)
server_socket.listen(5)

print(f"Listening on {host}:{port}")

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()

    print(f"Accepted connection from {client_address}")

    # Receive and print data from the client
    data = client_socket.recv(1024)
    if not data:
        break  # No more data received

    print(f"Received data: {data.decode('utf-8')}")

    # Close the client socket
    client_socket.close()

# Close the server socket when done
server_socket.close()
