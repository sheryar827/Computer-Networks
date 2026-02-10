# Simple TCP Client
# This connects to the server and receives a message

import socket

# Step 1: Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Connect to the server
# Must match the server's host and port
host = '127.0.0.1'
port = 5000
print(f"🔌 Connecting to server at {host}:{port}...")
client_socket.connect((host, port))
print("✅ Connected to server!")

# Step 3: Receive message from server
# 1024 = buffer size (how many bytes to receive at once)
message = client_socket.recv(1024).decode()  # decode() converts bytes to string
print(f"📥 Server says: {message}")

# Step 4: Close connection
client_socket.close()
print("👋 Disconnected from server")
