# Knock-Knock Joke Client
# This client follows the knock-knock joke protocol

import socket

# Connect to the joke server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5001))
print("🎭 Connected to Knock-Knock Joke Server!\n")

# STEP 1: Receive opening line
message = client_socket.recv(1024).decode()
print(f"Server: {message}")

# STEP 2: Respond with "Who's there?"
response = "Who's there?"
client_socket.send(response.encode())
print(f"You: {response}\n")

# STEP 3: Receive the name
message = client_socket.recv(1024).decode()
print(f"Server: {message}")

# STEP 4: Respond with "[name] who?"
response = f"{message} who?"
client_socket.send(response.encode())
print(f"You: {response}\n")

# STEP 5: Receive the punchline
message = client_socket.recv(1024).decode()
print(f"Server: {message}")
print("\n😄 Joke complete!")

# Close connection
client_socket.close()
print("👋 Disconnected")
