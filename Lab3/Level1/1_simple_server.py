# Simple TCP Server
# This is the most basic server - it accepts ONE client and sends a message

import socket

# Step 1: Create a socket
# AF_INET = IPv4, SOCK_STREAM = TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Bind to an address and port
# 127.0.0.1 = localhost (your own computer)
# 5000 = port number (choose any number above 1024)
host = '127.0.0.1'
port = 5000
server_socket.bind((host, port))

# Step 3: Listen for connections
# 1 = only 1 client can wait in queue
server_socket.listen(1)
print(f"✅ Server is listening on {host}:{port}")
print("⏳ Waiting for a client to connect...")

# Step 4: Accept connection from client
# This line WAITS until a client connects
client_socket, client_address = server_socket.accept()
print(f"🎉 Client connected from {client_address}")

# Step 5: Send a message to the client
message = "Welcome to my first TCP server! 🚀"
client_socket.send(message.encode())  # encode() converts string to bytes
print(f"📤 Sent message to client: {message}")

# Step 6: Close connections
client_socket.close()
server_socket.close()
print("👋 Server closed")
