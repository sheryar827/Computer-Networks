# UDP Multi-Client Server
# UDP is connectionless - server can receive from MANY clients without threading!

import socket

# Create UDP socket (notice SOCK_DGRAM instead of SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('127.0.0.1', 6000))

print("🌐 UDP Multi-Client Server started!")
print("📍 Listening on port 6000...")
print("✨ Can handle multiple clients simultaneously!\n")

client_count = {}  # Track how many messages from each client

while True:
    # Receive data from ANY client
    # recvfrom returns both data AND sender's address
    data, client_address = server_socket.recvfrom(1024)
    message = data.decode()

    # Track this client
    if client_address not in client_count:
        client_count[client_address] = 0
        print(f"🆕 New client: {client_address}")

    client_count[client_address] += 1

    print(f"📥 From {client_address}: {message}")
    print(f"   (Message #{client_count[client_address]} from this client)")

    # Send echo response back to this specific client
    response = f"Echo: {message}"
    server_socket.sendto(response.encode(), client_address)
    print(f"📤 Sent to {client_address}: {response}\n")

    # Show stats
    print(f"📊 Total unique clients: {len(client_count)}\n")
