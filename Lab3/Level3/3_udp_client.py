# UDP Client
# Simple client that sends messages to UDP server

import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 6000)

print("🌐 UDP Client started!")
print("💡 Type messages to send. Type 'exit' to quit.\n")

while True:
    # Get message from user
    message = input("Enter message: ")

    if message.lower() == 'exit':
        print("👋 Goodbye!")
        break

    # Send to server (no connection needed!)
    client_socket.sendto(message.encode(), server_address)

    # Receive response
    data, server = client_socket.recvfrom(1024)
    print(f"Server response: {data.decode()}\n")

client_socket.close()
